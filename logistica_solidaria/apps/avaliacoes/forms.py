from django import forms
from .models import Avaliacao


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota_geral', 'nota_atendimento', 'nota_prazo', 'comentario', 'recomendaria']
        widgets = {
            'nota_geral': forms.Select(choices=[(i, f'{i} estrela{"s" if i > 1 else ""}') for i in range(1, 6)], attrs={'class': 'w-full px-4 py-2.5 rounded-lg border border-gray-200 bg-gray-50 text-sm focus:outline-none focus:ring-2 focus:ring-primary'}),
            'nota_atendimento': forms.Select(choices=[(i, f'{i} estrela{"s" if i > 1 else ""}') for i in range(1, 6)], attrs={'class': 'w-full px-4 py-2.5 rounded-lg border border-gray-200 bg-gray-50 text-sm focus:outline-none focus:ring-2 focus:ring-primary'}),
            'nota_prazo': forms.Select(choices=[(i, f'{i} estrela{"s" if i > 1 else ""}') for i in range(1, 6)], attrs={'class': 'w-full px-4 py-2.5 rounded-lg border border-gray-200 bg-gray-50 text-sm focus:outline-none focus:ring-2 focus:ring-primary'}),
            'comentario': forms.Textarea(attrs={'class': 'w-full px-4 py-2.5 rounded-lg border border-gray-200 bg-gray-50 text-sm focus:outline-none focus:ring-2 focus:ring-primary', 'rows': 3, 'placeholder': 'Conte sua experiência...'}),
            'recomendaria': forms.CheckboxInput(attrs={'class': 'rounded text-primary'}),
        }
