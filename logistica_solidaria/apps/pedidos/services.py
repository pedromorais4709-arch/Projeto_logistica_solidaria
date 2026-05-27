import logging
from django.db import transaction
from django.utils import timezone
from apps.core.exceptions import (
    TransicaoStatusInvalida,
    PermissaoNegada,
    DoacaoIndisponivel,
)
from apps.rastreamento.models import EventoRastreamento
from apps.notificacoes.services import (
    notificar_pedido_criado,
    notificar_pedido_aprovado,
    notificar_status_atualizado,
)
 
logger = logging.getLogger('apps.pedidos')
 
TRANSICOES_VALIDAS = {
    'pendente':     ['aprovado', 'cancelado'],
    'aprovado':     ['em_separacao', 'cancelado'],
    'em_separacao': ['em_transito', 'cancelado'],
    'em_transito':  ['entregue', 'cancelado'],
    'entregue':     [],
    'cancelado':    [],
}
 
LABELS_STATUS = {
    'aprovado':     'Aprovar',
    'em_separacao': 'Iniciar separação',
    'em_transito':  'Enviar para entrega',
    'entregue':     'Confirmar entrega',
    'cancelado':    'Cancelar',
}
 
 
def proximos_status(status_atual):
    return [
        (s, LABELS_STATUS[s])
        for s in TRANSICOES_VALIDAS.get(status_atual, [])
    ]
 
 
def criar_pedido(beneficiario, doacao, dados):
    """
    Cria um pedido com validações completas.
    Raises: DoacaoIndisponivel, PermissaoNegada
    """
    logger.info(f'Criando pedido: usuario={beneficiario.pk} doacao={doacao.pk}')
 
    if not beneficiario.pode_pedir_doacao:
        raise PermissaoNegada('Apenas beneficiários e ONGs podem fazer pedidos.')
 
    if doacao.status != 'disponivel':
        raise DoacaoIndisponivel(f'A doação "{doacao.titulo}" não está mais disponível.')
 
    try:
        with transaction.atomic():
            from .models import Pedido
            pedido = Pedido.objects.create(
                beneficiario=beneficiario,
                doacao=doacao,
                quantidade_solicitada=dados.get('quantidade_solicitada', 1),
                justificativa=dados.get('justificativa', ''),
                observacoes=dados.get('observacoes', ''),
                prioridade=dados.get('prioridade', 'normal'),
            )
            EventoRastreamento.objects.create(
                pedido=pedido,
                tipo='criado',
                descricao='Pedido criado pelo beneficiário.',
                registrado_por=beneficiario,
                automatico=True,
            )
            logger.info(f'Pedido #{pedido.pk} criado com código {pedido.codigo_rastreio}')
            _notificar_silencioso(notificar_pedido_criado, pedido)
            return pedido
    except (DoacaoIndisponivel, PermissaoNegada):
        raise
    except Exception as e:
        logger.error(f'Erro ao criar pedido: {e}', exc_info=True)
        raise
 
 
def atualizar_status_pedido(pedido, novo_status, usuario, descricao=''):
    """
    Atualiza status com validação de transição.
    Raises: TransicaoStatusInvalida, PermissaoNegada
    """
    logger.info(f'Atualizando pedido #{pedido.pk}: {pedido.status} → {novo_status} por {usuario.pk}')
 
    if usuario.tipo not in ('admin', 'voluntario', 'doador') and usuario != pedido.doacao.doador:
        raise PermissaoNegada('Você não tem permissão para atualizar este pedido.')
 
    if novo_status not in TRANSICOES_VALIDAS.get(pedido.status, []):
        raise TransicaoStatusInvalida(
            f'Não é possível mudar de "{pedido.get_status_display()}" para "{novo_status}".'
        )
 
    try:
        with transaction.atomic():
            pedido.status = novo_status
 
            if novo_status == 'aprovado':
                pedido.data_aprovacao = timezone.now() if hasattr(pedido, 'data_aprovacao') else None
            elif novo_status == 'entregue':
                pedido.data_entrega = timezone.now()
                pedido.doacao.status = 'entregue'
                pedido.doacao.save(update_fields=['status'])
 
            pedido.save()
 
            EventoRastreamento.objects.create(
                pedido=pedido,
                tipo=novo_status,
                descricao=descricao or f'Status atualizado para {pedido.get_status_display()}.',
                registrado_por=usuario,
            )
 
            if novo_status == 'aprovado':
                _notificar_silencioso(notificar_pedido_aprovado, pedido)
            else:
                _notificar_silencioso(notificar_status_atualizado, pedido, novo_status)
 
            logger.info(f'Pedido #{pedido.pk} atualizado para {novo_status}')
            return pedido
 
    except (TransicaoStatusInvalida, PermissaoNegada):
        raise
    except Exception as e:
        logger.error(f'Erro ao atualizar pedido #{pedido.pk}: {e}', exc_info=True)
        raise
 
 
# ──────────────────────────────────────────────
# Funções para voluntário
# ──────────────────────────────────────────────
 
def aceitar_entrega(pedido, voluntario):
    """
    Voluntário aceita transportar um pedido aprovado.
    Raises: PermissaoNegada, TransicaoStatusInvalida
    """
    logger.info(f'Voluntário {voluntario.pk} aceitando entrega do pedido #{pedido.pk}')
 
    if not voluntario.e_voluntario:
        raise PermissaoNegada('Apenas voluntários podem aceitar entregas.')
 
    if pedido.status != 'aprovado':
        raise TransicaoStatusInvalida('Só é possível aceitar pedidos com status "aprovado".')
 
    if pedido.voluntario is not None:
        raise TransicaoStatusInvalida('Este pedido já tem um voluntário responsável.')
 
    with transaction.atomic():
        pedido.voluntario = voluntario
        pedido.status = 'em_separacao'
        pedido.save(update_fields=['voluntario', 'status', 'data_atualizacao'])
 
        EventoRastreamento.objects.create(
            pedido=pedido,
            tipo='em_separacao',
            descricao=f'Entrega aceita pelo voluntário {voluntario.get_full_name() or voluntario.username}.',
            registrado_por=voluntario,
        )
        _notificar_silencioso(notificar_status_atualizado, pedido, 'em_separacao')
 
    logger.info(f'Pedido #{pedido.pk} aceito por voluntário {voluntario.pk}')
    return pedido
 
 
def concluir_entrega(pedido, voluntario):
    """
    Voluntário confirma que a entrega foi realizada.
    Raises: PermissaoNegada, TransicaoStatusInvalida
    """
    logger.info(f'Voluntário {voluntario.pk} concluindo entrega do pedido #{pedido.pk}')
 
    if pedido.voluntario != voluntario and not voluntario.tipo == 'admin':
        raise PermissaoNegada('Você não é o voluntário responsável por esta entrega.')
 
    if pedido.status != 'em_transito':
        raise TransicaoStatusInvalida('Só é possível concluir pedidos com status "em trânsito".')
 
    with transaction.atomic():
        pedido.status = 'entregue'
        pedido.data_entrega = timezone.now()
        pedido.doacao.status = 'entregue'
        pedido.doacao.save(update_fields=['status'])
        pedido.save()
 
        EventoRastreamento.objects.create(
            pedido=pedido,
            tipo='entregue',
            descricao=f'Entrega confirmada pelo voluntário {voluntario.get_full_name() or voluntario.username}.',
            registrado_por=voluntario,
        )
        _notificar_silencioso(notificar_status_atualizado, pedido, 'entregue')
 
    logger.info(f'Pedido #{pedido.pk} entregue por voluntário {voluntario.pk}')
    return pedido
 
 
def _notificar_silencioso(func, *args, **kwargs):
    """Chama notificação sem deixar falha de email/notif quebrar o fluxo."""
    try:
        func(*args, **kwargs)
    except Exception as e:
        logger.warning(f'Falha ao enviar notificação ({func.__name__}): {e}')
 
