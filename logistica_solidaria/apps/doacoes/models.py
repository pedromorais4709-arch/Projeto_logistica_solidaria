from django.db import models
from django.conf import settings


class CategoriaDoacao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Doacao(models.Model):
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('reservado', 'Reservado'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ]

    CONDICAO_CHOICES = [
        ('novo', 'Novo'),
        ('semi_novo', 'Semi-novo'),
        ('usado_bom', 'Usado - Bom estado'),
        ('usado_regular', 'Usado - Estado regular'),
    ]

    doador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='doacoes_feitas'
    )
    categoria = models.ForeignKey(
        CategoriaDoacao,
        on_delete=models.PROTECT
    )
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    quantidade = models.PositiveIntegerField(default=1)
    condicao = models.CharField(max_length=20, choices=CONDICAO_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')
    imagem = models.ImageField(upload_to='doacoes/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Doação'
        verbose_name_plural = 'Doações'
        ordering = ['-data_criacao']

    def __str__(self):
        return f'{self.titulo} ({self.get_status_display()})'
