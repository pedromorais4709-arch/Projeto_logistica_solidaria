from django.contrib import admin
from .models import Pedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'beneficiario', 'doacao', 'status', 'prioridade', 'codigo_rastreio', 'data_criacao']
    list_filter = ['status', 'prioridade']
    search_fields = ['codigo_rastreio', 'beneficiario__username']
    readonly_fields = ['codigo_rastreio', 'data_criacao']
