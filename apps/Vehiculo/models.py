from django.db import models
from django.contrib import admin
# Create your models here.

class Vehiculo(models.Model):
    Placa= models.CharField(max_length = 45, primary_key=True)
    Modelo = models.CharField(max_length=45)
    Color = models.CharField(max_length = 45)
    Seguro = models.BooleanField()
    Tecnomecanica = models.BooleanField()

admin.site.register(Vehiculo)

