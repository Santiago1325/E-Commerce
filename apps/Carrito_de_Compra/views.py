from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from apps.Carrito_de_Compra.models import Carrito_de_Compra
from apps.Carrito_de_Compra.forms import CompraForm

# Create your views here.
def crearCompra(request, id_j):
    return render(request, 'registro/compraJuego.html')
