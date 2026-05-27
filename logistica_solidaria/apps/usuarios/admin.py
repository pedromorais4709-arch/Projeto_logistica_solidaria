from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ['username', 'email', 'tipo', 'cidade', 'estado', 'is_active']
    list_filter = ['tipo', 'is_active', 'estado']
    search_fields = ['username', 'email', 'cpf']
    fieldsets = UserAdmin.fieldsets + (
        ('Dados extras', {
            'fields': ('tipo', 'telefone', 'cpf', 'cidade', 'estado', 'foto', 'bio')
        }),
    )
