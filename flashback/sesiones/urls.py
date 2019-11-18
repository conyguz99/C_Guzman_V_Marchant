from django.urls import path
from .views import home, login, reservas, gracias, listado, eliminar, modificar


urlpatterns = [
   path('',home, name='home'),
   path('login/',login, name='login'),
   path('reservas/',reservas, name='reservas'),
   path('gracias/', gracias, name='gracias'),
   path('reservas/listado/', listado, name='listado'),
   path('eliminar/<id>/', eliminar, name='eliminar'),
   path('modificar/<id>/', modificar, name='modificar')
]

