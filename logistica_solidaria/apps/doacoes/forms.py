from django import forms
from .models import Doacao, CategoriaDoacao


class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = ['categoria', 'titulo', 'descricao', 'quantidade', 'condicao', 'imagem']
        widgets = {
            'categoria': forms.Select(attrs={'class': 'w-full px-4 py-2.5 rounded-lg border border-gray-200 bg-gray-50 text-sm focus:outline-none focus:ring-2 focus:ring-primary'}),
            'titulo': forms.TextInput(attrs={'class': 'w-full px-4 py-2.5 rounded-lg border border-gray-200 bg-gray-50 text-sm focus:outline-none focus:ring-2 focus:ring-primary', 'placeholder': 'Ex: Cesta básica com 10 itens'}),
            'descricao': forms.Textarea(attrs={'class': 'w-full px-4 py-2.5 rounded-lg border border-gray-200 bg-gray-50 text-sm focus:outline-none focus:ring-2 focus:ring-primary', 'rows': 4, 'placeholder': 'Descreva o que está doando...'}),
            'quantidade': forms.NumberInput(attrs={'class': 'w-full px-4 py-2.5 rounded-lg border border-gray-200 bg-gray-50 text-sm focus:outline-none focus:ring-2 focus:ring-primary'}),
            'condicao': forms.Select(attrs={'class': 'w-full px-4 py-2.5 rounded-lg border border-gray-200 bg-gray-50 text-sm focus:outline-none focus:ring-2 focus:ring-primary'}),
            'imagem': forms.FileInput(attrs={'class': 'w-full text-sm text-gray-500'}),
        }
