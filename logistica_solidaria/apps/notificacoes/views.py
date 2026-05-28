from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Notificacao
from django.utils import timezone


@login_required
def lista(request):
    notificacoes = Notificacao.objects.filter(destinatario=request.user).order_by('-data_criacao')
    nao_lidas = notificacoes.filter(lida=False).count()
    # Marca todas como lidas ao acessar a página
    notificacoes.filter(lida=False).update(lida=True, data_leitura=timezone.now())
    return render(request, 'notificacoes/lista.html', {
        'notificacoes': notificacoes,
        'nao_lidas': nao_lidas,
    })
