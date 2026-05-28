import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Pedido

logger = logging.getLogger('apps.pedidos')


@receiver(post_save, sender=Pedido)
def pedido_status_changed(sender, instance, created, **kwargs):
    if created:
        logger.info(f'Novo pedido criado: #{instance.pk} código={instance.codigo_rastreio}')
