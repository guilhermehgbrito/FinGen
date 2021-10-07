from django.db import models
from django.utils.timezone import now
from fin_gen.base.models.base import Base


class Atividade(Base):
    titulo              = models.CharField('Título', max_length=128)
    descricao           = models.CharField('Descrição', max_length=256)
    valor               = models.DecimalField('Valor', max_digits=14, decimal_places=2)
    moeda               = models.ForeignKey('fingen_financeiro.Moeda', on_delete=models.PROTECT)
    categoria           = models.ForeignKey('fingen_atividade.Categoria', on_delete=models.PROTECT)
    data_da_atividade   = models.DateTimeField('Data de vigência', default=now)
