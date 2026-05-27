from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    TIPO_CHOICES = [
        ('doador', 'Doador'),
        ('beneficiario', 'Beneficiário'),
        ('voluntario', 'Voluntário'),
        ('ong', 'ONG'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='doador')
    telefone = models.CharField(max_length=20, blank=True)
    cpf = models.CharField(max_length=14, blank=True, null=True, unique=True)
    cnpj = models.CharField(max_length=18, blank=True, null=True, unique=True)
    razao_social = models.CharField(max_length=200, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    foto = models.ImageField(upload_to='usuarios/fotos/', blank=True, null=True)
    bio = models.TextField(blank=True)
    # Campos de ONG
    pagina_titulo = models.CharField(max_length=200, blank=True)
    pagina_descricao = models.TextField(blank=True)
    pagina_missao = models.TextField(blank=True)
    pagina_historia = models.TextField(blank=True)
    pagina_publicada = models.BooleanField(default=False)
    # Campos de voluntário
    tipo_veiculo = models.CharField(max_length=50, blank=True)
    placa_veiculo = models.CharField(max_length=10, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return f'{self.get_full_name() or self.username} ({self.get_tipo_display()})'

    @property
    def pode_pedir_doacao(self):
        return self.tipo in ('beneficiario', 'ong')

    @property
    def pode_doar(self):
        return self.tipo == 'doador'

    @property
    def e_voluntario(self):
        return self.tipo == 'voluntario'

    @property
    def e_ong(self):
        return self.tipo == 'ong'
