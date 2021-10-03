from django.db import models
from fin_gen.base.models.base import Base


class Icone(Base):
    descricao   = models.CharField('Descrição', max_length=32, unique=True)
    valor       = models.CharField('Código', max_length=32, unique=True)
