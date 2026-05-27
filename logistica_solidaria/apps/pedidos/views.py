import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Pedido
from .forms import PedidoForm
from .services import (
    criar_pedido,
    atualizar_status_pedido,
    proximos_status,
    aceitar_entrega as service_aceitar,
    concluir_entrega as service_concluir,
)
from apps.doacoes.models import Doacao
from apps.core.exceptions import (
    TransicaoStatusInvalida,
    PermissaoNegada,
    DoacaoIndisponivel,
)
 
logger = logging.getLogger('apps.pedidos')
 
 
@login_required
def lista(request):
    user = request.user
    if user.tipo in ('admin', 'voluntario'):
        pedidos = Pedido.objects.select_related('beneficiario', 'doacao').all()
    elif user.tipo == 'doador':
        pedidos = Pedido.objects.filter(doacao__doador=user).select_related('beneficiario', 'doacao')
    else:
        pedidos = Pedido.objects.filter(beneficiario=user).select_related('doacao')
 
    status = request.GET.get('status', '')
    if status:
        pedidos = pedidos.filter(status=status)
 
    return render(request, 'pedidos/lista.html', {
        'pedidos': pedidos.order_by('-data_criacao'),
        'status_filtro': status,
        'status_choices': Pedido.STATUS_CHOICES,
    })
 
 
@login_required
def detalhe(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    eventos = pedido.eventos.order_by('data_evento')
    user = request.user
    pode_atualizar = user.tipo in ('admin', 'voluntario', 'doador') or user == pedido.doacao.doador
    return render(request, 'pedidos/detalhe.html', {
        'pedido': pedido,
        'eventos': eventos,
        'pode_atualizar': pode_atualizar and pedido.status not in ('entregue', 'cancelado'),
        'proximos_status': proximos_status(pedido.status),
    })
 
 
@login_required
def novo(request, doacao_pk):
    doacao = get_object_or_404(Doacao, pk=doacao_pk)
 
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            try:
                pedido = criar_pedido(request.user, doacao, form.cleaned_data)
                messages.success(request, f'Pedido #{pedido.pk} criado! Código: {pedido.codigo_rastreio}')
                return redirect('pedidos:detalhe', pk=pedido.pk)
            except PermissaoNegada as e:
                messages.error(request, str(e))
            except DoacaoIndisponivel as e:
                messages.error(request, str(e))
            except Exception:
                logger.error('Erro inesperado ao criar pedido', exc_info=True)
                messages.error(request, 'Erro inesperado. Tente novamente.')
    else:
        form = PedidoForm()
 
    return render(request, 'pedidos/form.html', {'form': form, 'doacao': doacao})
 
 
@login_required
def atualizar_status(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    novo_status = request.POST.get('status')
    descricao = request.POST.get('descricao', '')
 
    try:
        atualizar_status_pedido(pedido, novo_status, request.user, descricao)
        messages.success(request, 'Status atualizado com sucesso!')
    except TransicaoStatusInvalida as e:
        messages.error(request, str(e))
    except PermissaoNegada as e:
        messages.error(request, str(e))
    except Exception:
        logger.error(f'Erro inesperado ao atualizar pedido #{pk}', exc_info=True)
        messages.error(request, 'Erro inesperado. Tente novamente.')
 
    return redirect('pedidos:detalhe', pk=pk)
 
 
@login_required
def aceitar_entrega(request, pk):
    """Voluntário aceita transportar o pedido."""
    if request.method != 'POST':
        return redirect('pedidos:detalhe', pk=pk)
 
    pedido = get_object_or_404(Pedido, pk=pk)
    try:
        service_aceitar(pedido, request.user)
        messages.success(request, f'Entrega aceita! Pedido #{pedido.pk} está sob sua responsabilidade.')
    except (PermissaoNegada, TransicaoStatusInvalida) as e:
        messages.error(request, str(e))
    except Exception:
        logger.error(f'Erro ao aceitar entrega pedido #{pk}', exc_info=True)
        messages.error(request, 'Erro inesperado. Tente novamente.')
 
    return redirect('relatorios:dashboard')
 
 
@login_required
def concluir_entrega(request, pk):
    """Voluntário confirma que entregou o pedido."""
    if request.method != 'POST':
        return redirect('pedidos:detalhe', pk=pk)
 
    pedido = get_object_or_404(Pedido, pk=pk)
    try:
        service_concluir(pedido, request.user)
        messages.success(request, f'Entrega #{pedido.pk} concluída com sucesso!')
    except (PermissaoNegada, TransicaoStatusInvalida) as e:
        messages.error(request, str(e))
    except Exception:
        logger.error(f'Erro ao concluir entrega pedido #{pk}', exc_info=True)
        messages.error(request, 'Erro inesperado. Tente novamente.')
 
    return redirect('relatorios:dashboard')
 
