from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms.fields import EmailField
from fin_gen.apps.fingen_usuario.models import Usuario


class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('email',)
