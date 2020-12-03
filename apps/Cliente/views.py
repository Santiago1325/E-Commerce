from django.shortcuts import render
from django.http import HttpResponse
from apps.Cliente.models import Cliente
from apps.Cliente.forms import ClienteForm

#def index(request):
#    return render(request, 'registro/inicio.html')


def crearCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        form.save()
    else:
        form = ClienteForm()
    return render(request, 'registro/inicio.html', {'form':form})