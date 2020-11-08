from django.db import models
from apps.Videojuego.models import Videojuego
from apps.Genero.models import Genero
from django.contrib import admin
# Create your models here.


class Genero_Videojuego(models.Model):
    Codigo_Video_Juegos = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    ID_Genero = models.ForeignKey(Genero, on_delete=models.CASCADE)


admin.site.register(Genero_Videojuego)
