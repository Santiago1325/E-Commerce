from django.db import models
from django.contrib import admin

# Create your models here.

class Cliente(models.Model):
    Identificacion = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=45)
    Apellido = models.CharField(max_length=45)
    Correo = models.CharField(max_length=45)
    Contraseña = models.CharField(max_length=45)

admin.site.register(Cliente)