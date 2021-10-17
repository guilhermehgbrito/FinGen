from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic.base import TemplateView
from fin_gen.apps.fingen_usuario.views.editar import edita_senha, edita_usuario

from .forms import UsuarioAuthForm
from .views import registro

urlpatterns = [
    path('login', LoginView.as_view(template_name='fingen_usuario/login.html', form_class=UsuarioAuthForm, redirect_authenticated_user=True), name='login'),
    path('logout', LogoutView.as_view(), name="logout"),
    path('registro', registro, name="registro"),
    path('editar', edita_usuario, name="edita_usuario"),
    path('senha', edita_senha, name="edita_senha")
]
