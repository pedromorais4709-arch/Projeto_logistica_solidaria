from django.contrib import admin
from .models import CategoriaDoacao, Doacao


@admin.register(CategoriaDoacao)
class CategoriaDoacaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ativo']
    search_fields = ['nome']


@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'doador', 'categoria', 'status', 'condicao', 'data_criacao']
    list_filter = ['status', 'condicao', 'categoria']
    search_fields = ['titulo', 'doador__username']
