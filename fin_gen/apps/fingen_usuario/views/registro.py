from django.contrib.auth import login
from django.contrib.auth.models import AnonymousUser
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from fin_gen.apps.fingen_usuario.forms import UsuarioCreationForm
from fin_gen.apps.fingen_usuario.models.usuario import Usuario


def registro(request):
    if not isinstance(request.user, AnonymousUser):
        return redirect("index")
    if request.method == "POST":
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        else:
            return redirect("registro")
    else:
        return render(request, "fingen_usuario/registro.html")
