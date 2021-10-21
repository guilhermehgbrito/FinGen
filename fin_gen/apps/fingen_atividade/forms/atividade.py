from django import forms
from fin_gen.apps.fingen_atividade.models import Atividade
from fin_gen.apps.fingen_financeiro.models import Carteira


class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        exclude = ['ativo']
        
        widgets = {
            "carteira": forms.Select(choices=Carteira.objects.all()),
            "data_da_atividade": forms.SelectDateWidget()
        }
