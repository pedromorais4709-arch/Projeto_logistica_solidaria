import logging
from apps.core.exceptions import PedidoJaAvaliado, PermissaoNegada
from apps.notificacoes.services import notificar_avaliacao_recebida

logger = logging.getLogger('apps.avaliacoes')


def criar_avaliacao(pedido, avaliador, dados):
    """
    Cria avaliação com validações.
    Raises: PedidoJaAvaliado, PermissaoNegada
    """
    logger.info(f'Criando avaliação: pedido={pedido.pk} avaliador={avaliador.pk}')

    if pedido.beneficiario != avaliador:
        raise PermissaoNegada('Apenas o beneficiário pode avaliar este pedido.')

    if pedido.status != 'entregue':
        raise PermissaoNegada('Só é possível avaliar pedidos entregues.')

    if hasattr(pedido, 'avaliacao'):
        raise PedidoJaAvaliado('Este pedido já foi avaliado.')

    try:
        from .models import Avaliacao
        avaliacao = Avaliacao.objects.create(
            pedido=pedido,
            avaliador=avaliador,
            nota_geral=dados.get('nota_geral'),
            nota_atendimento=dados.get('nota_atendimento'),
            nota_prazo=dados.get('nota_prazo'),
            comentario=dados.get('comentario', ''),
            recomendaria=dados.get('recomendaria'),
        )
        logger.info(f'Avaliação #{avaliacao.pk} criada com nota {avaliacao.nota_geral}')
        try:
            notificar_avaliacao_recebida(avaliacao)
        except Exception as e:
            logger.warning(f'Falha ao notificar avaliação: {e}')
        return avaliacao
    except (PedidoJaAvaliado, PermissaoNegada):
        raise
    except Exception as e:
        logger.error(f'Erro ao criar avaliação: {e}', exc_info=True)
        raise
