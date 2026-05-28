from django.db import models
from django.conf import settings
from apps.pedidos.models import Pedido


class EventoRastreamento(models.Model):
    TIPO_CHOICES = [
        ('criado', 'Pedido criado'),
        ('aprovado', 'Aprovado'),
        ('em_separacao', 'Em separação'),
        ('em_transito', 'Em trânsito'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
        ('observacao', 'Observação'),
    ]

    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='eventos'
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.TextField()
    localizacao = models.CharField(max_length=200, blank=True)
    registrado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    automatico = models.BooleanField(default=False)
    data_evento = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Evento de Rastreamento'
        verbose_name_plural = 'Eventos de Rastreamento'
        ordering = ['-data_evento']

    def __str__(self):
        return f'{self.pedido} → {self.get_tipo_display()}'
