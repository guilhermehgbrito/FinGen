from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)
from fin_gen.apps.fingen_usuario.models import Usuario


class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'telefone', 'username', 'email')

class UsuarioAuthForm(AuthenticationForm):
    username = forms.EmailField(max_length=256)
