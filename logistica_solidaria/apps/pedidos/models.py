from django.db import models
from django.conf import settings
from apps.doacoes.models import Doacao
 
 
class Pedido(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('em_separacao', 'Em separação'),
        ('em_transito', 'Em trânsito'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ]
 
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('normal', 'Normal'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ]
 
    beneficiario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='pedidos_recebidos'
    )
    doacao = models.ForeignKey(
        Doacao,
        on_delete=models.PROTECT,
        related_name='pedidos'
    )

    voluntario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='entregas',
        null=True,
        blank=True,
        verbose_name='Voluntário responsável',
    )
    quantidade_solicitada = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='normal')
    justificativa = models.TextField()
    observacoes = models.TextField(blank=True)
    codigo_rastreio = models.CharField(max_length=50, unique=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    data_entrega = models.DateTimeField(null=True, blank=True)
 
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-data_criacao']
 
    def __str__(self):
        return f'Pedido #{self.pk} - {self.beneficiario} ({self.get_status_display()})'
 
    def save(self, *args, **kwargs):
        if not self.codigo_rastreio:
            import uuid
            self.codigo_rastreio = f'LS{uuid.uuid4().hex[:8].upper()}'
        super().save(*args, **kwargs)
 
    @property
    def disponivel_para_voluntario(self):
        """Pedido aprovado ainda sem voluntário atribuído."""
        return self.status == 'aprovado' and self.voluntario is None
 
