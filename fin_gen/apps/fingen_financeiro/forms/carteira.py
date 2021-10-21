from django import forms
from fin_gen.apps.fingen_financeiro.models import Carteira


class CarteiraForm(forms.ModelForm):
    class Meta:
        model = Carteira
        exclude = ['id', 'ativo']

        widgets = {
            'usuario': forms.HiddenInput()
        }
