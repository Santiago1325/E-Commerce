from django.db import models
from django.contrib import admin
from apps.Vehiculo.models import Vehiculo
# Create your models here.

class Domiciliario(models.Model):
    ID_Domiciliario = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=45)
    Apellido = models.CharField(max_length = 45)
    Placa_Vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)


admin.site.register(Domiciliario)
