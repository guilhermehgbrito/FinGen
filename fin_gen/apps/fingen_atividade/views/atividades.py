from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from fin_gen.apps.fingen_atividade.forms import AtividadeForm
from fin_gen.apps.fingen_atividade.models import Atividade
from fin_gen.apps.fingen_financeiro.models import Carteira


@login_required
def lista_atividades(request):
    atividades = Atividade.objects.filter(carteira__usuario=request.user)
    return render(request, "fingen_atividade/atividades/lista.html", {"atividades": atividades})

@login_required
def cria_atividade(request):
    if request.method == "POST":
        form = AtividadeForm(request.POST)
        if form.is_valid():
            atividade = form.save()
            messages.success(request, f"Atividade \"{atividade.titulo}\" criada com sucesso!")
            return redirect('lista_atividades')
        else:
            messages.error(request, "Erro ao gravar dados.")
            return redirect('lista_atividades')
    else:
        form = AtividadeForm()
        form.fields["carteira"].queryset = Carteira.objects.filter(usuario=request.user)
        return render(request, "fingen_atividade/atividades/criar_editar.html", {"form": form, "modo": "cria"})

@login_required
def edita_atividade(request, id):
    try:
        atividade = Atividade.objects.get(pk=id)
        if atividade.carteira.usuario != request.user:
            return redirect('lista_atividades')
        if request.method == "POST":
            form = AtividadeForm(request.POST, instance=atividade)
            if form.is_valid():
                atividade = form.save()
                messages.success(request, f"Atividade \"{atividade.titulo}\" editada com sucesso!")
                return redirect('lista_atividades')
            else:
                messages.error(request, "Erro ao gravar dados.")
                return redirect('lista_atividades')
        else:
            form = AtividadeForm(instance=atividade)
            form.fields["carteira"].queryset = Carteira.objects.filter(usuario=request.user)
            return render(request, "fingen_atividade/atividades/criar_editar.html", {"form": form, "modo": "edita", "atividade_id": atividade.id})
    except Atividade.DoesNotExist:
        return redirect('lista_atividades')


@login_required
def exclui_atividade(request, id):
    try:
        atividade = Atividade.objects.get(pk=id)
        if atividade.carteira.usuario != request.user:
            return redirect('lista_atividades')
        else:
            atividade.delete()
            messages.success(request, "Atividade excluida com sucesso!")
            return redirect('lista_atividades')
    except Atividade.DoesNotExist:
        return redirect('lista_atividades')
    
