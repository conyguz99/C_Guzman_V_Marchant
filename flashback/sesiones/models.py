from django.db import models
from django.urls import reverse
# Create your models here.

class Tipo(models.Model):
    sesion = models.CharField(max_length = 50)
    
    def __str__(self):
      return self.sesion


class Reserva(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    fecha = models.DateTimeField(auto_now_add = False)
    email = models.EmailField(max_length =500)
    Tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(blank = True, null= True)

    LOAN_STATUS = (
     ('D','disponible'),
     ('R','reservado'),
    )

    status = models.CharField(
    max_length = 1,
    choices = LOAN_STATUS,
    blank = False,
    default = 'D',
    )