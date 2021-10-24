from django import forms
from fin_gen.apps.fingen_atividade.models import Atividade
from fin_gen.apps.fingen_financeiro.forms import carteira


class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        exclude = ['ativo']
        
        widgets = {
            "carteira": forms.Select(),
            "data_da_atividade": forms.SelectDateWidget()
        }
    def clean(self):
        self.update = self.instance.pk is not None
        if self.update:
            valor = self.instance.valor
            tipo = self.instance.tipo
            carteira = self.instance.carteira
            update_tipo = False
            update_valor = False
            update_carteira = False
            if 'tipo' in self.changed_data:
                update_tipo = True    
                tipo_update = self.cleaned_data['tipo']    
            if 'valor' in self.changed_data:
                update_valor = True    
                valor_update = self.cleaned_data['valor']
            if 'carteira' in self.changed_data:
                update_carteira = True    
                carteira_update = self.cleaned_data['carteira']    
            if update_carteira and update_tipo and update_valor:
                if tipo == 'D':
                    valor *= -1
                carteira.saldo -= valor
                carteira.save()
                if tipo_update == 'D':
                    valor_update *= -1
                carteira_update.saldo += valor_update
                carteira_update.save()
            elif update_carteira and update_tipo:
                valor_aux = valor
                if tipo == 'D':
                    valor *= -1
                carteira.saldo -= valor
                carteira.save()
                if tipo_update == 'D':
                    valor_aux *= -1
                carteira_update.saldo += valor_aux
                carteira_update.save()
            elif update_carteira and update_valor:
                if tipo == 'D':
                    valor *= -1
                    valor_update *= -1
                carteira.saldo -= valor
                carteira.save()
                carteira_update.saldo += valor_update
                carteira_update.save()
            elif update_tipo and update_valor:
                if tipo == 'D':
                    valor *= -1
                carteira.saldo -= valor
                if tipo_update == 'D':
                    valor_update *= -1
                carteira.saldo += valor_update
                carteira.save()
            elif update_carteira:
                if tipo == 'D':
                    valor *= -1
                carteira.saldo -= valor
                carteira.save()
                carteira_update.saldo += valor
                carteira_update.save()
            elif update_tipo:
                valor_aux = valor
                if tipo == 'D':
                    valor *= -1
                carteira.saldo -= valor
                if tipo_update == 'D':
                    valor_aux *= -1
                carteira.saldo += valor_aux
                carteira.save()
            elif update_valor:
                if tipo == 'D':
                    valor *= -1
                    valor_update *= -1
                carteira.saldo -= valor
                carteira.saldo += valor_update
                carteira.save()
        return super().clean()
    
    def save(self, commit=True):
        atividade = super().save(commit=commit)
        if self.update:
            return atividade
        else:
            valor = atividade.valor
            if atividade.tipo == 'D':
                valor *= -1
            atividade.carteira.saldo += valor
            atividade.carteira.save()
        return atividade
