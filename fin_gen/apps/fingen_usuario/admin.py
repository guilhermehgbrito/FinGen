from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from fin_gen.apps.fingen_usuario.forms import (UsuarioChangeForm,
                                               UsuarioCreationForm)

from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'username')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}))
    add_fieldsets = (None, {
            'classes': ('wide',),
            'fields': ('email', 'telefone', 'is_staff', 'is_superuser', 'password1', 'password2'),
        }),
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm
