from django.urls import path
from apps.Videojuego.views import consultarJuegos, editarJuego, crearJuego

urlpatterns = [
    path('consultarJuegos', consultarJuegos, name='consultarJuegos'),
    path('editarJuego/<id_j>', editarJuego, name='editarJuego'),
    path('crearJuego', crearJuego, name='crearJuego')
]