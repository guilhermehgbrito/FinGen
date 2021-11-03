from django.db import models
from django.utils.timezone import now
from fin_gen.base.models.base import Base


class Atividade(Base):
    TIPO_CHOICES = (("P", "Proventos"), ("D", "Descontos"))

    titulo = models.CharField("Título", max_length=128)
    descricao = models.CharField("Descrição", max_length=256)
    valor = models.DecimalField("Valor", max_digits=14, decimal_places=2)
    moeda = models.ForeignKey(
        "fingen_financeiro.Moeda", on_delete=models.PROTECT
    )
    categoria = models.ForeignKey(
        "fingen_atividade.Categoria", on_delete=models.PROTECT
    )
    data_da_atividade = models.DateField("Data de vigência", default=now)
    tipo = models.CharField(
        "Provento/Desconto", max_length=1, choices=TIPO_CHOICES, default="P"
    )
    carteira = models.ForeignKey(
        "fingen_financeiro.Carteira", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.titulo

    def delete(self, using=None, keep_parents=False):
        valor = self.valor
        if self.tipo == "P":
            valor *= -1
        self.carteira.saldo += valor
        self.carteira.save()
        return super().delete(using=using, keep_parents=keep_parents)
