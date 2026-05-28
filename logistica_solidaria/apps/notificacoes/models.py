from django.db import models
from django.conf import settings


class Notificacao(models.Model):
    TIPO_CHOICES = [
        ('pedido_criado', 'Pedido criado'),
        ('pedido_aprovado', 'Pedido aprovado'),
        ('pedido_em_transito', 'Pedido em trânsito'),
        ('pedido_entregue', 'Pedido entregue'),
        ('nova_doacao', 'Nova doação disponível'),
        ('avaliacao_recebida', 'Avaliação recebida'),
        ('sistema', 'Notificação do sistema'),
    ]

    destinatario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notificacoes'
    )
    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES)
    titulo = models.CharField(max_length=200)
    mensagem = models.TextField()
    lida = models.BooleanField(default=False)
    data_leitura = models.DateTimeField(null=True, blank=True)
    link = models.CharField(max_length=500, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Notificação'
        verbose_name_plural = 'Notificações'
        ordering = ['-data_criacao']

    def __str__(self):
        return f'{self.titulo} → {self.destinatario}'

    def marcar_como_lida(self):
        from django.utils import timezone
        self.lida = True
        self.data_leitura = timezone.now()
        self.save(update_fields=['lida', 'data_leitura'])
