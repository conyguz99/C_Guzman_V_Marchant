from django.contrib import admin

# Register your models here.

from . models import Tipo, Reserva

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','fecha','email','telefono','Tipo','descripcion','status')
    search_fields = ['Tipo','status']

admin.site.register(Tipo)
admin.site.register(Reserva, ReservaAdmin)
