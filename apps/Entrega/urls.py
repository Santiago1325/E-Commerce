from django.urls import path
from apps.Entrega.views import crearEntrega

urlpatterns = [
 path('crearEntrega', crearEntrega, name= 'crearEntrega'),
]