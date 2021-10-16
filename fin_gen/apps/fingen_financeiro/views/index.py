import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from fin_gen.apps.fingen_atividade import models
from fin_gen.apps.fingen_atividade.models import *
from fin_gen.apps.fingen_financeiro.models import *
from fin_gen.apps.fingen_financeiro.utils import (
    atitivades_categories_percentage, atividades_mean,
    group_atividades_by_month, group_atividades_by_selected_year,
    group_atividades_by_year, is_empty)


@login_required
def index(request):
    carteiras = Carteira.objects.filter(usuario=request.user, ativo=True)
    saldo_carteiras = carteiras.values_list('saldo', flat=True)
    saldo_total = sum(saldo_carteiras)
    atividades = Atividade.objects.filter(carteira__in=carteiras, ativo=True)
    atividades_month_group = is_empty(atividades, group_atividades_by_month)
    media_mensal = is_empty(atividades_month_group, atividades_mean)
    atividades_categories = is_empty(atividades, atitivades_categories_percentage)
    atividades_year_group = is_empty(atividades, group_atividades_by_year)
    atividades_year_month_group = is_empty(atividades, group_atividades_by_selected_year)
    atividades_line = is_empty(atividades_year_month_group, json.dumps, ensure_ascii=False)
    ganho_anual = is_empty(atividades_year_group, atividades_mean)

    context = {
        'saldo': saldo_total,
        'atividades_categorias': atividades_categories,
        'atividades': len(atividades),
        'media_mensal': media_mensal,
        'ganho_anual': ganho_anual,
        'atividades_line': atividades_line
    }
    return render(request, 'fingen_financeiro/index.html', context)
