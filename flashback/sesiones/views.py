from django.shortcuts import render
from .models import Tipo, Reserva
# Create your views here.
def home(request):
	num_Reserva = Reserva.objects.all().count()

	num_reserva_lista = Reserva.objects.filter(status__exact='R').count()

	return render(
		request, 
		'home.html', 
		context = {'num_Reserva': num_Reserva, 'num_reserva_lista': num_reserva_lista} 
    )
