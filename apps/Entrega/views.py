from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from apps.Entrega.models import Entrega
from apps.Entrega.forms import EntregaForm
from django.shortcuts import render

# Create your views here.
def crearEntrega(request):
    if request.method == 'POST':
        form = EntregaForm(request.POST)
        form.save()
    else:
        form = EntregaForm()
    return render(request, 'registro/crearEntrega.html', {'form':form})