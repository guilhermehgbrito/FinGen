from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from fin_gen.apps.fingen_usuario.forms import (UsuarioChangeTemplate,
                                               UsuarioPasswordChangeForm)


@login_required
def edita_usuario(request):
    form = UsuarioChangeTemplate(instance=request.user)
    if request.method == "POST":
        form = UsuarioChangeTemplate(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Dados alterados com sucesso!")
            return redirect("index")
        else:
            messages.error(request, "Erro ao gravar dados.")
            return redirect("index")
    else:
        return render(request, "fingen_usuario/editar.html", {"form": form})

@login_required
def edita_senha(request):
    form = UsuarioPasswordChangeForm(request.user)
    if request.method == "POST":
        form = UsuarioPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Senha alterada com sucesso!")
            return redirect("index")
        else:
            messages.error(request, "Erro ao gravar dados.")
            return redirect("index")
    else:
        return render(request, "fingen_usuario/editar_senha.html", {"form": form})
