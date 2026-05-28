from django.contrib import admin
from .models import EventoRastreamento


@admin.register(EventoRastreamento)
class EventoRastreamentoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'tipo', 'registrado_por', 'automatico', 'data_evento']
    list_filter = ['tipo', 'automatico']
    search_fields = ['pedido__codigo_rastreio']
