from django.core.mail import send_mail
from django.conf import settings
from .models import Notificacao


def criar_notificacao(destinatario, tipo, titulo, mensagem, link=''):
    Notificacao.objects.create(
        destinatario=destinatario,
        tipo=tipo,
        titulo=titulo,
        mensagem=mensagem,
        link=link,
    )


def notificar_e_emailar(destinatario, tipo, titulo, mensagem, link='', corpo_email=''):
    criar_notificacao(destinatario, tipo, titulo, mensagem, link)
    try:
        send_mail(
            subject=f'[Logística Solidária] {titulo}',
            message=corpo_email or mensagem,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[destinatario.email],
            fail_silently=True,
        )
    except Exception:
        pass


def notificar_pedido_criado(pedido):
    notificar_e_emailar(
        pedido.doacao.doador,
        'pedido_criado',
        'Novo pedido recebido!',
        f'{pedido.beneficiario.get_full_name() or pedido.beneficiario.username} solicitou sua doação "{pedido.doacao.titulo}".',
        link=f'/pedidos/{pedido.pk}/',
        corpo_email=f'''
Olá {pedido.doacao.doador.get_full_name() or pedido.doacao.doador.username},

Você recebeu um novo pedido para sua doação "{pedido.doacao.titulo}".

Solicitante: {pedido.beneficiario.get_full_name() or pedido.beneficiario.username}
Justificativa: {pedido.justificativa}

Acesse o sistema para aprovar ou recusar: http://127.0.0.1:8000/pedidos/{pedido.pk}/

Equipe Logística Solidária
        ''',
    )


def notificar_pedido_aprovado(pedido):
    notificar_e_emailar(
        pedido.beneficiario,
        'pedido_aprovado',
        'Seu pedido foi aprovado! 🎉',
        f'O pedido #{pedido.pk} ({pedido.doacao.titulo}) foi aprovado.',
        link=f'/pedidos/{pedido.pk}/',
        corpo_email=f'''
Olá {pedido.beneficiario.get_full_name() or pedido.beneficiario.username},

Ótima notícia! Seu pedido #{pedido.pk} para "{pedido.doacao.titulo}" foi aprovado.

Código de rastreio: {pedido.codigo_rastreio}
Acompanhe em: http://127.0.0.1:8000/rastreamento/{pedido.codigo_rastreio}/

Equipe Logística Solidária
        ''',
    )


def notificar_status_atualizado(pedido, novo_status):
    msgs = {
        'em_separacao': 'Seu pedido está sendo separado.',
        'em_transito': 'Seu pedido saiu para entrega! 🚚',
        'entregue': 'Sua entrega foi realizada! Que tal avaliar? ⭐',
        'cancelado': 'Seu pedido foi cancelado.',
    }
    mensagem = msgs.get(novo_status, f'Status atualizado para: {novo_status}')
    notificar_e_emailar(
        pedido.beneficiario,
        f'pedido_{novo_status}',
        f'Atualização do pedido #{pedido.pk}',
        mensagem,
        link=f'/rastreamento/{pedido.codigo_rastreio}/',
        corpo_email=f'''
Olá {pedido.beneficiario.get_full_name() or pedido.beneficiario.username},

{mensagem}

Pedido: #{pedido.pk} — {pedido.doacao.titulo}
Rastreio: {pedido.codigo_rastreio}
Acompanhe em: http://127.0.0.1:8000/rastreamento/{pedido.codigo_rastreio}/

Equipe Logística Solidária
        ''',
    )


def notificar_avaliacao_recebida(avaliacao):
    notificar_e_emailar(
        avaliacao.pedido.doacao.doador,
        'avaliacao_recebida',
        'Você recebeu uma avaliação!',
        f'Sua doação "{avaliacao.pedido.doacao.titulo}" foi avaliada com {avaliacao.nota_geral}/5 estrelas.',
        link=f'/avaliacoes/',
    )
