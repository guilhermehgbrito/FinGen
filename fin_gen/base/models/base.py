from django.db import models


class Base(models.Model):
    ativo = models.BooleanField('Ativo', default=True)
    criado_em = models.DateTimeField('Data de criação', auto_now_add=True)
    atualizado_em = models.DateTimeField('Última atualização', auto_now=True)

    class Meta:
        abstract = True
