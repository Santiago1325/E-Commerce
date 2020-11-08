from django.db import models
from django.contrib import admin

# Create your models here.
class Clasificacion_Edad(models.Model):
    ID_Clasificacion = models.CharField(primary_key=True,max_length=2)
    Nombre = models.CharField(max_length=45)

admin.site.register(Clasificacion_Edad)
