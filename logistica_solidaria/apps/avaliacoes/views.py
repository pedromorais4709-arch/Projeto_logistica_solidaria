import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Avaliacao
from .forms import AvaliacaoForm
from .services import criar_avaliacao
from apps.pedidos.models import Pedido
from apps.core.exceptions import PedidoJaAvaliado, PermissaoNegada

logger = logging.getLogger('apps.avaliacoes')


@login_required
def lista(request):
    avaliacoes = Avaliacao.objects.select_related('pedido__doacao', 'avaliador').all()
    return render(request, 'avaliacoes/lista.html', {'avaliacoes': avaliacoes})


@login_required
def nova(request, pedido_pk):
    pedido = get_object_or_404(Pedido, pk=pedido_pk)

    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            try:
                criar_avaliacao(pedido, request.user, form.cleaned_data)
                messages.success(request, 'Avaliação enviada! Obrigada pelo feedback. ⭐')
                return redirect('pedidos:detalhe', pk=pedido_pk)
            except PedidoJaAvaliado as e:
                messages.warning(request, str(e))
                return redirect('pedidos:detalhe', pk=pedido_pk)
            except PermissaoNegada as e:
                messages.error(request, str(e))
            except Exception:
                logger.error('Erro inesperado ao criar avaliação', exc_info=True)
                messages.error(request, 'Erro inesperado. Tente novamente.')
    else:
        form = AvaliacaoForm()

    return render(request, 'avaliacoes/form.html', {'form': form, 'pedido': pedido})
