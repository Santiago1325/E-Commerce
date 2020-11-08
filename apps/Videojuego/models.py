from django.db import models
from apps.Desarrollador.models import Desarrollador
from django.contrib import admin
from apps.Plataforma.models import Plataforma
from apps.Clasificacion_Edad.models import Clasificacion_Edad
from apps.Franquicia.models import Franquicia
# Create your models here.

class Videojuego(models.Model):
    Codigo = models.IntegerField(primary_key=True)
    Multijugador = models.BooleanField()
    Costo = models.IntegerField()
    Nombre = models.CharField(max_length=45)
    ID_Desarrollador = models.ForeignKey(Desarrollador, on_delete=models.CASCADE)
    ID_Plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    ID_Clasificacion_de_edad = models.ForeignKey(Clasificacion_Edad, on_delete=models.CASCADE)
    ID_Admin = models.IntegerField()
    ID_Franquicia = models.ForeignKey(Franquicia, on_delete=models.CASCADE)


admin.site.register(Videojuego)
