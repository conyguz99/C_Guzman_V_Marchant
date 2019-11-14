from django.contrib import admin

# Register your models here.

from . models import Tipo, Reserva

admin.site.register(Tipo)
admin.site.register(Reserva)