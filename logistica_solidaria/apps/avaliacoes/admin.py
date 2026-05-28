from django.contrib import admin
from .models import Avaliacao


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'avaliador', 'nota_geral', 'nota_atendimento', 'nota_prazo', 'data_avaliacao']
    list_filter = ['nota_geral']
    search_fields = ['pedido__codigo_rastreio', 'avaliador__username']
