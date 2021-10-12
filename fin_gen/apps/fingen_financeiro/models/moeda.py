from django.db import models
from django.db.utils import ProgrammingError
from fin_gen.base.models.base import Base


class Moeda(Base):
    codigo = models.CharField('Código', max_length=3, help_text='Código da moeda. Ex: USD, BRL, EUR, etc.')
    nome = models.CharField('Nome', max_length=64)
    simbolo = models.CharField('Símbolo monetátio', max_length=4, help_text='Símbolo monetário. Ex: R$, C$', null=True)


def moeda_default():
    try:
        moeda = Moeda.objects.get_or_create(codigo="BRL", defaults={"nome": "Real brasileiro", "simbolo": "R$"})
        return moeda[0].id
    except ProgrammingError:
        return None
