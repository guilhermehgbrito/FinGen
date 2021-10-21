from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from fin_gen.apps.fingen_financeiro.forms import CarteiraForm
from fin_gen.apps.fingen_financeiro.models import Carteira


@login_required
def lista_carteiras(request):
    carteiras = Carteira.objects.filter(usuario=request.user, ativo=True)
    return render(request, 'fingen_financeiro/carteiras/lista.html', {'carteiras': carteiras})

@login_required
def cria_carteira(request):
    carteiras = Carteira.objects.filter(usuario=request.user, ativo=True)
    if len(carteiras) >= 3:
        return redirect('lista_carteiras')
    if request.method == "POST":
        form = CarteiraForm(request.POST)
        if form.is_valid():
            carteira = form.save()
            messages.success(request, f'A carteira "{carteira.nome}" foi criada com sucesso!')            
            return redirect('lista_carteiras')
        else:
            messages.error(request, f'Erro ao criar carteira!')
            return render(request, 'fingen_financeiro/carteiras/criar_editar.html', {"form": form}, status=400)

    else:
        form = CarteiraForm(initial={'usuario': request.user.id})
        return render(request, 'fingen_financeiro/carteiras/criar_editar.html', {"form": form, "modo": 'cria'})

@login_required
def edita_carteira(request, id):
    carteira = Carteira.objects.get(pk=id)
    if request.method == "POST":
        form = CarteiraForm(request.POST, instance=carteira)
        if form.is_valid():
            carteira = form.save()
            messages.success(request, f'A carteira "{carteira.nome}" foi editada com sucesso!')            
            return redirect('lista_carteiras')
        else:
            messages.error(request, f'Erro ao editar carteira!')
            return render(request, 'fingen_financeiro/carteiras/criar_editar.html', {"form": form}, status=400)

    else:
        form = CarteiraForm(instance=carteira)
        return render(request, 'fingen_financeiro/carteiras/criar_editar.html', {"form": form, "modo": "edita", "carteira_id": carteira.id})


@login_required
def exclui_carteira(request, id):
    try:
        carteira = Carteira.objects.get(pk=id)
        if carteira.usuario != request.user:
            messages.error(request, "Erro ao deletar!")
            return redirect('lista_carteiras')
        carteira.delete()
        messages.success(request, "Carteira deletada com sucesso!")
        return redirect('lista_carteiras')
    except:
        return redirect('lista_carteiras')
