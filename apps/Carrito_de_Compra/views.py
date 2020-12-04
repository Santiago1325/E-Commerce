from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from apps.Carrito_de_Compra.models import Carrito_de_Compra
from apps.Carrito_de_Compra.forms import CompraForm

# Create your views here.
def crearCompra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        form.save()
    else:
        form = CompraForm()
    return render(request, 'registro/compraJuego.html', {'form':form})
