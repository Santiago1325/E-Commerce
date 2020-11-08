from django.db import models
from django.contrib import admin
from apps.Cliente.models import Cliente

# Create your models here.

class Direccion(models.Model):
    ID_Direccion = models.IntegerField(primary_key=True)
    Direccion = models.CharField(max_length=45)
    Identificacion_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

admin.site.register(Direccion)
