from django.urls import path
from apps.Domiciliario.views import consultarDomiciliario, crearDomiciliario, editarDom, eliminarDom

urlpatterns = [
 path('consultarDomiciliario', consultarDomiciliario, name= 'consultarDomiciliario'),
 path('crearDomiciliario', crearDomiciliario, name = 'crearDomiciliario'),
 path('editarDomiciliario/<id_dom>', editarDom, name = 'editarDomiciliario'),
 path('eliminarDomiciliario/<id_dom>' ,eliminarDom, name = 'eliminarDomiciliario'),
]
