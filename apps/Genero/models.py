from django.db import models
from django.contrib import admin
# Create your models here.

class Genero(models.Model):
    ID_Genero = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=45)

admin.site.register(Genero)


