from django.urls import path

from .views import (
    cria_atividade,
    edita_atividade,
    exclui_atividade,
    lista_atividades,
)

urlpatterns = [
    path("", lista_atividades, name="lista_atividades"),
    path("criar", cria_atividade, name="cria_atividade"),
    path("editar/<int:id>", edita_atividade, name="edita_atividade"),
    path("excluir/<int:id>", exclui_atividade, name="exclui_atividade"),
]
