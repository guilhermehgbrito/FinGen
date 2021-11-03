from django.urls import path
from fin_gen.apps.fingen_relatorio.views import (
    atividades_por_carteira,
    atividades_por_categoria,
    atividades_por_periodo,
    lista_relatorios,
)

urlpatterns = [
    path("", lista_relatorios, name="lista_relatorios"),
    path(
        "atividades-carteira",
        atividades_por_carteira,
        name="atividades_por_carteira",
    ),
    path(
        "atividades-categoria",
        atividades_por_categoria,
        name="atividades_por_categoria",
    ),
    path(
        "atividades-periodo",
        atividades_por_periodo,
        name="atividades_por_periodo",
    ),
]
