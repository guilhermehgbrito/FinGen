from django.contrib.auth import get_user_model
from django.db import models
from fin_gen.base.models.base import Base


class Carteira(Base):
    nome = models.CharField("Nome", max_length=128)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    saldo = models.DecimalField('Saldo', max_digits=15, decimal_places=2, default=0)
