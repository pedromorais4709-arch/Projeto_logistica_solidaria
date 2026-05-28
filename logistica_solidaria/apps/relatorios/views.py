from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.pedidos.models import Pedido
from apps.doacoes.models import Doacao
from apps.avaliacoes.models import Avaliacao
from django.db.models import Avg


@login_required
def dashboard(request):
    user = request.user

    if user.tipo == 'doador':
        return _dashboard_doador(request)
    elif user.tipo in ('beneficiario', 'ong'):
        return _dashboard_beneficiario(request)
    elif user.tipo == 'voluntario':
        return _dashboard_voluntario(request)
    else:
        return _dashboard_admin(request)


def _dashboard_doador(request):
    user = request.user
    minhas_doacoes = Doacao.objects.filter(doador=user).order_by('-data_criacao')[:5]
    stats = {
        'total': Doacao.objects.filter(doador=user).count(),
        'disponiveis': Doacao.objects.filter(doador=user, status='disponivel').count(),
        'entregues': Doacao.objects.filter(doador=user, status='entregue').count(),
    }
    return render(request, 'relatorios/dashboard_doador.html', {
        'stats': stats,
        'minhas_doacoes': minhas_doacoes,
    })


def _dashboard_beneficiario(request):
    user = request.user
    meus_pedidos = Pedido.objects.filter(beneficiario=user).order_by('-data_criacao')[:5]
    stats = {
        'total_pedidos': Pedido.objects.filter(beneficiario=user).count(),
        'pendentes': Pedido.objects.filter(beneficiario=user, status='pendente').count(),
        'entregues': Pedido.objects.filter(beneficiario=user, status='entregue').count(),
        'pagina_publicada': user.e_ong and user.pagina_publicada,
    }
    return render(request, 'relatorios/dashboard_beneficiario.html', {
        'stats': stats,
        'meus_pedidos': meus_pedidos,
    })


def _dashboard_voluntario(request):
    return render(request, 'relatorios/dashboard_voluntario.html')


def _dashboard_admin(request):
    media = Avaliacao.objects.aggregate(m=Avg('nota_geral'))['m'] or 0
    stats_list = [
        ('Total de Doações',    Doacao.objects.count(),                           f"{Doacao.objects.filter(status='disponivel').count()} disponíveis", '📦'),
        ('Total de Pedidos',    Pedido.objects.count(),                           f"{Pedido.objects.filter(status='pendente').count()} pendentes",     '📋'),
        ('Entregas Realizadas', Pedido.objects.filter(status='entregue').count(), 'pedidos concluídos',                                                '✅'),
        ('Média de Avaliação',  f'{media:.1f}',                                   'de 5 estrelas',                                                     '⭐'),
    ]
    pedidos_recentes = Pedido.objects.select_related('beneficiario', 'doacao').order_by('-data_criacao')[:5]
    return render(request, 'relatorios/dashboard.html', {
        'stats_list': stats_list,
        'pedidos_recentes': pedidos_recentes,
    })
