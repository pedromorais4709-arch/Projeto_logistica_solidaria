import logging
from apps.core.exceptions import PermissaoNegada, DoacaoIndisponivel

logger = logging.getLogger('apps.doacoes')


def criar_doacao(doador, dados, imagem=None):
    """Cria doação com validações."""
    logger.info(f'Criando doação: doador={doador.pk}')

    if not doador.pode_doar:
        raise PermissaoNegada('Apenas doadores podem cadastrar doações.')

    try:
        from .models import Doacao
        doacao = Doacao(
            doador=doador,
            categoria=dados.get('categoria'),        # ← objeto direto
            titulo=dados.get('titulo'),
            descricao=dados.get('descricao'),
            quantidade=dados.get('quantidade', 1),
            condicao=dados.get('condicao'),
        )
        if imagem:
            doacao.imagem = imagem
        doacao.save()
        logger.info(f'Doação #{doacao.pk} criada: {doacao.titulo}')
        return doacao
    except PermissaoNegada:
        raise
    except Exception as e:
        logger.error(f'Erro ao criar doação: {e}', exc_info=True)
        raise


def cancelar_doacao(doacao, usuario):
    """Cancela doação se ainda disponível."""
    if doacao.doador != usuario and usuario.tipo != 'admin':
        raise PermissaoNegada('Você não pode cancelar esta doação.')

    if doacao.status not in ('disponivel', 'reservado'):
        raise DoacaoIndisponivel('Esta doação não pode ser cancelada.')

    doacao.status = 'cancelado'
    doacao.save(update_fields=['status'])
    logger.info(f'Doação #{doacao.pk} cancelada por {usuario.pk}')
    return doacao
