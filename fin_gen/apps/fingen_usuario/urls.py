from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .forms import UsuarioAuthForm

urlpatterns = [
    path('login', LoginView.as_view(template_name='fingen_usuario/login.html', form_class=UsuarioAuthForm, redirect_authenticated_user=True), name='login'),
    path('logout', LogoutView.as_view(), name="logout")
]
