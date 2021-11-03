from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from fin_gen.apps.fingen_atividade.models import Atividade, Categoria
from fin_gen.apps.fingen_financeiro.models import Carteira
from weasyprint import HTML


@login_required
def lista_relatorios(request):
    categorias = Categoria.objects.all()
    carteiras = Carteira.objects.filter(usuario=request.user)

    context = {
        "categorias": categorias,
        "carteiras": carteiras,
    }
    return render(request, "fingen_relatorio/lista_relatorios.html", context)


@login_required
def atividades_por_carteira(request):
    if request.method == "POST":
        try:
            data_inicio = date(
                *[int(x) for x in request.POST["data-inicio"].split("-")]
            )
            data_fim = date(
                *[int(x) for x in request.POST["data-fim"].split("-")]
            )
            filtrar_periodo = True
        except ValueError:
            filtrar_periodo = False

        try:
            carteira = Carteira.objects.get(
                pk=int(request.POST["carteira"]), usuario=request.user
            )
        except Carteira.DoesNotExist:
            messages.error(request, "Carteira inexistente.")
            return redirect("lista_relatorios")

        atividades = (
            Atividade.objects.select_related("categoria")
            .filter(carteira=carteira)
            .order_by("-data_da_atividade")
        )

        if filtrar_periodo:
            atividades = atividades.filter(
                data_da_atividade__range=[data_inicio, data_fim]
            )

        if len(atividades) == 0:
            messages.warning(
                request, "Não existem resultados para os filtros requisitados."
            )
            return redirect("lista_relatorios")

        total_atividades = sum(
            [x.valor if x.tipo == "P" else x.valor * -1 for x in atividades]
        )

        context = {
            "atividades": atividades,
            "carteira": carteira,
            "total_atividades": total_atividades,
            "tipo_de_relatorio": "Atividades por Carteira",
            "filtrar_periodo": filtrar_periodo,
            "user": request.user,
        }

        if filtrar_periodo:
            context["data_de_inicio"] = data_inicio
            context["data_de_fim"] = data_fim

        html_string = render_to_string(
            "fingen_relatorio/pdfs/lista_atividades_por_carteira.html", context
        )
        pdf_file = HTML(string=html_string).write_pdf()
        response = HttpResponse(pdf_file, content_type="application/pdf")
        response["Content-Disposition"] = 'inline; filename="relatorio.pdf"'
        response["Content-Encoding"] = "binary"

        return response
    else:
        return redirect("lista_relatorios")


@login_required
def atividades_por_categoria(request):
    if request.method == "POST":
        try:
            data_inicio = date(
                *[int(x) for x in request.POST["data-inicio"].split("-")]
            )
            data_fim = date(
                *[int(x) for x in request.POST["data-fim"].split("-")]
            )
            filtrar_periodo = True
        except ValueError:
            filtrar_periodo = False

        try:
            categoria = Categoria.objects.get(
                pk=int(request.POST["categoria"])
            )
        except ValueError:
            messages.error(request, "Categoria inexistente.")
            return redirect("lista_relatorios")

        atividades = (
            Atividade.objects.select_related("categoria")
            .filter(categoria=categoria, carteira__usuario=request.user)
            .order_by("-data_da_atividade")
        )

        if filtrar_periodo:
            atividades = atividades.filter(
                data_da_atividade__range=[data_inicio, data_fim]
            )

        if len(atividades) == 0:
            messages.warning(
                request, "Não existem resultados para os filtros requisitados."
            )
            return redirect("lista_relatorios")

        total_atividades = sum(
            [x.valor if x.tipo == "P" else x.valor * -1 for x in atividades]
        )

        context = {
            "atividades": atividades,
            "total_atividades": total_atividades,
            "categoria": categoria,
            "tipo_de_relatorio": "Atividades por Categoria",
            "filtrar_periodo": filtrar_periodo,
            "user": request.user,
        }

        html_string = render_to_string(
            "fingen_relatorio/pdfs/lista_atividades_por_categoria.html",
            context,
        )
        pdf_file = HTML(string=html_string).write_pdf()
        response = HttpResponse(pdf_file, content_type="application/pdf")
        response["Content-Disposition"] = 'inline; filename="relatorio.pdf"'
        response["Content-Encoding"] = "binary"

        return response
    else:
        return redirect("lista_relatorios")


@login_required
def atividades_por_periodo(request):
    if request.method == "POST":
        try:
            data_inicio = date(
                *[int(x) for x in request.POST["data-inicio"].split("-")]
            )
            data_fim = date(
                *[int(x) for x in request.POST["data-fim"].split("-")]
            )
            filtrar_periodo = True
        except ValueError:
            messages.error(request, "Data inválida.")
            return redirect("lista_relatorios")

        atividades = (
            Atividade.objects.select_related("categoria")
            .filter(data_da_atividade__range=[data_inicio, data_fim])
            .order_by("-data_da_atividade")
        )

        if len(atividades) == 0:
            messages.warning(
                request, "Não existem resultados para os filtros requisitados."
            )
            return redirect("lista_relatorios")

        total_atividades = sum(
            [x.valor if x.tipo == "P" else x.valor * -1 for x in atividades]
        )

        context = {
            "data_de_inicio": data_inicio,
            "data_de_fim": data_fim,
            "atividades": atividades,
            "total_atividades": total_atividades,
            "tipo_de_relatorio": "Atividades por Período",
            "filtrar_periodo": filtrar_periodo,
            "user": request.user,
        }

        html_string = render_to_string(
            "fingen_relatorio/pdfs/lista_atividades_por_periodo.html", context
        )
        pdf_file = HTML(string=html_string).write_pdf()
        response = HttpResponse(pdf_file, content_type="application/pdf")
        response["Content-Disposition"] = 'inline; filename="relatorio.pdf"'
        response["Content-Encoding"] = "binary"

        return response
    else:
        return redirect("lista_relatorios")
