from django import forms
from .models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['quantidade_solicitada', 'justificativa', 'observacoes', 'prioridade']
        widgets = {
            'quantidade_solicitada': forms.NumberInput(attrs={'class': 'w-full px-4 py-2.5 rounded-lg border border-gray-200 bg-gray-50 text-sm focus:outline-none focus:ring-2 focus:ring-primary'}),
            'justificativa': forms.Textarea(attrs={'class': 'w-full px-4 py-2.5 rounded-lg border border-gray-200 bg-gray-50 text-sm focus:outline-none focus:ring-2 focus:ring-primary', 'rows': 4, 'placeholder': 'Por que você precisa desta doação?'}),
            'observacoes': forms.Textarea(attrs={'class': 'w-full px-4 py-2.5 rounded-lg border border-gray-200 bg-gray-50 text-sm focus:outline-none focus:ring-2 focus:ring-primary', 'rows': 2, 'placeholder': 'Informações adicionais (opcional)'}),
            'prioridade': forms.Select(attrs={'class': 'w-full px-4 py-2.5 rounded-lg border border-gray-200 bg-gray-50 text-sm focus:outline-none focus:ring-2 focus:ring-primary'}),
        }
