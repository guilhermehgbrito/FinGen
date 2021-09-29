from uuid import uuid4

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UsuarioManager(BaseUserManager):
    def _create_user(self, email, password,  **kwargs):
        user  = self.model(
            email = email,
            **kwargs
        )
        user.set_password(password)
        user.save(using   = self.db)
        return user


    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('O campo e-mail deve ser informado')

        kwargs.setdefault('is_superuser', False)

        email = self.normalize_email(email)

        return self._create_user(email, password, **kwargs)
        

    def create_superuser(self, email, password, **kwargs):
        if not email:
            raise ValueError('O campo e-mail deve ser informado')

        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        email = self.normalize_email(email)

        return self._create_user(email, password, **kwargs)


class Usuario(AbstractUser):
    id              = models.UUIDField('Id', primary_key=True, unique=True, default=uuid4)
    telefone        = models.CharField('Telefone', max_length=11, unique=True)
    email           = models.EmailField('E-mail', unique=True)
    is_staff        = models.BooleanField('Equipe', default=False)
    criado_em       = models.DateTimeField('Data de criação', auto_now_add=True)
    atualizado_em   = models.DateTimeField('Última atualização', auto_now=True)

    objects         = UsuarioManager()

    USERNAME_FIELD  = 'email'

    REQUIRED_FIELDS = ['telefone']
