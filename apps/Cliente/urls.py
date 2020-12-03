from django.urls import path
from apps.Cliente.views import crearCliente, sesion

urlpatterns = [
 path('crearCliente', crearCliente, name= 'crearCliente'),
 path('', sesion, name = 'sesion')
]
