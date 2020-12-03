from django.shortcuts import render
from django.http import HttpResponse
from apps.Cliente.models import Cliente
from apps.Cliente.forms import ClienteForm
from django.contrib.auth.decorators import login_required

#def index(request):
#    return render(request, 'registro/inicio.html')


@login_required
def sesion(request):
    if request.user.groups.filter(name='Cliente').exists():
        return render(request, 'registro/sesionCliente.html')
    else:
        return render(request, 'registro/sesionAdministrador.html')

def crearCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        form.save()
    else:
        form = ClienteForm()
    return render(request, 'registro/inicio.html', {'form':form})