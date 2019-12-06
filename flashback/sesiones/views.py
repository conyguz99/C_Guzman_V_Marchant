from django.shortcuts import render, redirect
from .models import Tipo, Reserva
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request,'login.html')

def registrarse(request):
    return render(request,'registrarse.html')

@login_required
def reservas(request):
    tipo = Tipo.objects.all()
    variables = {'tipo': tipo}
#con esto guardaremos las reservas
    if request.POST:
        reserva = Reserva()
        reserva.nombre = request.POST.get("Nombre")
        reserva.apellido = request.POST.get("Apellido")
        reserva.fecha = request.POST.get("Fecha")
        reserva.email = request.POST.get("Correo")
        reserva.telefono = request.POST.get("Telefono")
        tipo = Tipo()
        tipo.id = request.POST.get("Tipo")
        reserva.tipo= tipo
        reserva.descripcion = request.POST.get("Comentario")
        reserva.status = request.POST.get("status")

        try: 
            reserva.save()
            variables['mensaje'] = 'Guardado correctamente'

        except:

            variables['mensaje'] = 'No se ha podido guardar'

    return render(request, 'reservas.html', variables)

def gracias(request):
    return render(request, 'gracias.html')

#CRUD de Reservas
def listado(request):

    reserva = Reserva.objects.all()
    
    return render(request, 'listado.html',{'reserva': reserva})

def eliminar(request, id):

    reserva = Reserva.objects.get(id=id)
     
    try: 
        reserva.delete()
        mensaje = "Reserva eliminada correctamente"
        messages.success(request, mensaje)
    except: 
        mensaje = "No se ha podido eliminar"
        messages.error(request, mensaje)

    return redirect('listado')

def modificar(request, id):
    #buscamos la reserva para que el usuario lo pueda modificar
    reserva = Reserva.objects.get(id=id)
    tipo = Tipo.objects.all()

    variables = {
      'reserva': reserva,
      'tipo': tipo
    }

    if request.POST:
        reserva = Reserva()
        reserva.id = request.POST.get("id")
        reserva.nombre = request.POST.get("Nombre")
        reserva.apellido = request.POST.get("Apellido")
        reserva.fecha = request.POST.get("Fecha")
        reserva.email = request.POST.get("Correo")
        reserva.telefono = request.POST.get("Telefono")
        tipo = Tipo()
        tipo.id = request.POST.get("Tipo")
        reserva.Tipo= tipo
        reserva.descripcion = request.POST.get("Comentario")
        reserva.status = request.POST.get("status")

        try: 
            reserva.save()
            messages.success(request, 'Modificado correctamente')

        except:

            messages.error(request, 'No se ha podido modificar')
            
        return redirect('listado')

    return render(request, 'modificar.html', variables)