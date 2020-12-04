from django.urls import path
from apps.Entrega.views import crearEntrega, consultarEntrega

urlpatterns = [
 path('crearEntrega', crearEntrega, name= 'crearEntrega'),
 path('consultarEntrega', consultarEntrega, name='consultarEntrega'),
]