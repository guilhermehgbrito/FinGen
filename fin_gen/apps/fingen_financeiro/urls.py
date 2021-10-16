from django.urls import path
from fin_gen.apps.fingen_financeiro.views.carteira import edita_carteira

from .views import cria_carteira, exclui_carteira, index, lista_carteiras

urlpatterns = [
    path('', index, name='index'),
    path('carteiras', lista_carteiras, name="lista_carteiras"),
    path('carteiras/criar', cria_carteira, name="cria_carteira"),
    path('carteiras/editar/<int:id>', edita_carteira, name="edita_carteira"),
    path('carteiras/excluir/<int:id>', exclui_carteira, name="exclui_carteira")
]
