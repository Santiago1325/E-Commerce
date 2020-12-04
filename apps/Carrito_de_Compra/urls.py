from django.urls import path
from apps.Carrito_de_Compra.views import crearCompra

urlpatterns = [
    path('crearCompra', crearCompra, name='crearCompra'),
]