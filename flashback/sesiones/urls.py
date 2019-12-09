from django.urls import path
from .views import home,login,logout,registrarse, reservas, gracias, listado, eliminar, modificar


urlpatterns = [
   path('',home, name='home'),
   path('login/',login,name='login'),
   path('logout/',logout,name='logout'),
   path('registrarse/',registrarse, name='registrarse'),
   path('reservas/',reservas, name='reservas'),
   path('gracias/', gracias, name='gracias'),
   path('listado/', listado, name='listado'),
   path('eliminar/<id>/', eliminar, name='eliminar'),
   path('modificar/<id>/', modificar, name='modificar')
]

