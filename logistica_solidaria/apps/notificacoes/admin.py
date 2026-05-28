from django.contrib import admin
from .models import Notificacao


@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'destinatario', 'tipo', 'lida', 'data_criacao']
    list_filter = ['tipo', 'lida']
    search_fields = ['titulo', 'destinatario__username']
