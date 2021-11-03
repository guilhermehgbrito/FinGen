from django.core.validators import MinLengthValidator
from django.db import models
from fin_gen.base.models.base import Base


class Categoria(Base):
    titulo = models.CharField("Título", max_length=128, unique=True)
    icone = models.ForeignKey(
        "fingen_atividade.Icone", on_delete=models.PROTECT
    )
    cor = models.CharField(
        "Cor",
        help_text="Valor em hexadecimal. Ex:#FFFFFF",
        max_length=7,
        validators=[MinLengthValidator(7)],
    )

    def __str__(self) -> str:
        return self.titulo
