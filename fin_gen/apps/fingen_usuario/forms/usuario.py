from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       UserChangeForm, UserCreationForm)
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

class UsuarioChangeTemplate(forms.ModelForm):
    first_name = forms.CharField(max_length=128, required=True, label="Primeiro Nome")
    last_name = forms.CharField(max_length=128, required=True, label="Sobrenome")
    telefone = forms.CharField(max_length=11, min_length=11, required=True)
    class Meta:
        model = Usuario
        fields = ('email', 'first_name', 'last_name', 'telefone', 'username')

class UsuarioPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = Usuario
