from django.urls import path
from apps.Cliente.views import crearCliente

urlpatterns = [
 path('crearCliente', crearCliente, name= 'crearCliente'),
]
