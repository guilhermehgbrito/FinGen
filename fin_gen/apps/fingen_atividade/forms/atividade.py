from django import forms
from fin_gen.apps.fingen_atividade.models import Atividade


class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        exclude = ['ativo']
        
        widgets = {
            "carteira": forms.Select(),
            "data_da_atividade": forms.SelectDateWidget()
        }
