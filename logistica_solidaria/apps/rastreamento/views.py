from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.pedidos.models import Pedido

@login_required
def consulta(request):
    pedido = None
    codigo = request.GET.get('codigo', '')
    if codigo:
        try:
            pedido = Pedido.objects.get(codigo_rastreio=codigo)
        except Pedido.DoesNotExist:
            pedido = None
    return render(request, 'rastreamento/consulta.html', {'pedido': pedido, 'codigo': codigo})

@login_required
def detalhe(request, codigo):
    pedido = get_object_or_404(Pedido, codigo_rastreio=codigo)
    eventos = pedido.eventos.order_by('data_evento')
    return render(request, 'rastreamento/detalhe.html', {'pedido': pedido, 'eventos': eventos})
