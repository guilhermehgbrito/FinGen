from django.contrib import admin

from .models import Carteira, Moeda

admin.site.register(Moeda)
admin.site.register(Carteira)
