from django.shortcuts import render, redirect
from .models import Tipo, Reserva
from django.contrib import messages
from .forms import CustomeUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
     return render(request, 'login.html')

def logout(request):
     return render(request, 'logout.html')

def registro(request):
    data = {'form':CustomeUserForm()}

    if request.method == 'POST':
        formulario = CustomeUserForm(request.POST)
        if formulario.is_valid():
         formulario.save()
         #autenticar al usuario y redirigirlo al inicio

        Username = formulario.cleaned_data[ 'Username' ]
        password = formulario.cleaned_data[ 'password1' ]
        user = authenticate(Username=Username, password=password1) 
        login(request, user)
        return redirect(to= 'home')

    return render(request,'registrarse.html', data)
@login_required()
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
@permission_required('sesiones.view_reservas')
def listado(request):

    reserva = Reserva.objects.all()
    
    return render(request, 'listado.html',{'reserva': reserva})

@permission_required('sesiones.delete_reservas')
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

@permission_required('sesiones.change_reservas')
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