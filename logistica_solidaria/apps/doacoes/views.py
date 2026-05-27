import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Doacao, CategoriaDoacao
from .forms import DoacaoForm
from .services import criar_doacao, cancelar_doacao
from apps.core.exceptions import PermissaoNegada, DoacaoIndisponivel

logger = logging.getLogger('apps.doacoes')


@login_required
def lista(request):
    doacoes = Doacao.objects.select_related('doador', 'categoria').all()
    status = request.GET.get('status', '')
    categoria = request.GET.get('categoria', '')
    if status:
        doacoes = doacoes.filter(status=status)
    if categoria:
        doacoes = doacoes.filter(categoria_id=categoria)
    categorias = CategoriaDoacao.objects.filter(ativo=True)
    return render(request, 'doacoes/lista.html', {
        'doacoes': doacoes,
        'categorias': categorias,
        'status_filtro': status,
        'categoria_filtro': categoria,
    })


@login_required
def detalhe(request, pk):
    doacao = get_object_or_404(Doacao, pk=pk)
    return render(request, 'doacoes/detalhe.html', {'doacao': doacao})


@login_required
def nova(request):
    if request.method == 'POST':
        form = DoacaoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                doacao = criar_doacao(
                    request.user,
                    form.cleaned_data,
                    imagem=request.FILES.get('imagem'),
                )
                messages.success(request, f'Doação "{doacao.titulo}" cadastrada com sucesso!')
                return redirect('doacoes:detalhe', pk=doacao.pk)
            except PermissaoNegada as e:
                messages.error(request, str(e))
            except Exception:
                logger.error('Erro inesperado ao criar doação', exc_info=True)
                messages.error(request, 'Erro inesperado. Tente novamente.')
    else:
        form = DoacaoForm()
    return render(request, 'doacoes/form.html', {'form': form, 'titulo': 'Nova Doação'})


@login_required
def editar(request, pk):
    doacao = get_object_or_404(Doacao, pk=pk, doador=request.user)
    if request.method == 'POST':
        form = DoacaoForm(request.POST, request.FILES, instance=doacao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doação atualizada!')
            return redirect('doacoes:detalhe', pk=doacao.pk)
    else:
        form = DoacaoForm(instance=doacao)
    return render(request, 'doacoes/form.html', {'form': form, 'titulo': 'Editar Doação', 'doacao': doacao})


@login_required
def cancelar(request, pk):
    doacao = get_object_or_404(Doacao, pk=pk)
    try:
        cancelar_doacao(doacao, request.user)
        messages.success(request, 'Doação cancelada.')
    except PermissaoNegada as e:
        messages.error(request, str(e))
    except DoacaoIndisponivel as e:
        messages.error(request, str(e))
    return redirect('doacoes:lista')
