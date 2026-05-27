from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuario


def home(request):
    if request.user.is_authenticated:
        return redirect('relatorios:dashboard')
    return render(request, 'home.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('relatorios:dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('relatorios:dashboard')
        messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'usuarios/login.html')


def logout_view(request):
    logout(request)
    return redirect('usuarios:home')


def cadastro_view(request):
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        tipo = request.POST.get('tipo', 'doador')

        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'usuarios/cadastro.html')

        email = request.POST.get('email')
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado.')
            return render(request, 'usuarios/cadastro.html')

        # Campos específicos por tipo
        if tipo == 'ong':
            first_name = request.POST.get('first_name_ong', '')
            razao_social = request.POST.get('razao_social', '')
            cnpj = request.POST.get('cnpj') or None
            telefone = request.POST.get('telefone_ong', '')
        else:
            first_name = request.POST.get('first_name', '')
            razao_social = ''
            cnpj = None
            telefone = request.POST.get('telefone', '')

        user = Usuario.objects.create_user(
            username=email,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=request.POST.get('last_name', ''),
            tipo=tipo,
            telefone=telefone,
            cpf=request.POST.get('cpf') or None,
            cnpj=cnpj,
            razao_social=razao_social,
            cidade=request.POST.get('cidade', ''),
            estado=request.POST.get('estado', ''),
            tipo_veiculo=request.POST.get('tipo_veiculo', ''),
            placa_veiculo=request.POST.get('placa_veiculo', ''),
        )
        login(request, user)
        messages.success(request, f'Bem-vinda, {user.first_name or user.email}!')
        return redirect('relatorios:dashboard')

    return render(request, 'usuarios/cadastro.html')


@login_required
def perfil_view(request):
    return render(request, 'usuarios/perfil.html', {'usuario': request.user})


@login_required
def pagina_ong_view(request):
    if not request.user.e_ong:
        messages.error(request, 'Acesso restrito a ONGs.')
        return redirect('relatorios:dashboard')

    if request.method == 'POST':
        user = request.user
        user.pagina_titulo = request.POST.get('pagina_titulo', '')
        user.pagina_descricao = request.POST.get('pagina_descricao', '')
        user.pagina_missao = request.POST.get('pagina_missao', '')
        user.pagina_historia = request.POST.get('pagina_historia', '')
        user.pagina_publicada = True
        user.save()
        messages.success(request, 'Página pública atualizada!')
        return redirect('usuarios:pagina_ong')

    return render(request, 'usuarios/pagina_ong.html', {'usuario': request.user})


def paginas_ongs(request):
    """Lista todas as ONGs com página publicada."""
    from .models import Usuario
    ongs = Usuario.objects.filter(tipo='ong', pagina_publicada=True)
    return render(request, 'usuarios/paginas_ongs.html', {'ongs': ongs})


def pagina_publica_ong(request, pk):
    """Página pública de uma ONG específica."""
    from .models import Usuario
    from apps.pedidos.models import Pedido
    ong = Usuario.objects.get(pk=pk, tipo='ong', pagina_publicada=True)
    pedidos_abertos = Pedido.objects.filter(
        beneficiario=ong,
        status='pendente'
    ).select_related('doacao')
    return render(request, 'usuarios/pagina_publica_ong.html', {
        'ong': ong,
        'pedidos_abertos': pedidos_abertos,
    })
