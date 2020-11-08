from django.db import models
from django.contrib import admin
from apps.Cliente.models import Cliente
from apps.Domiciliario.models import Domiciliario

# Create your models here.
class Carrito_de_Compra(models.Model):
    ID_Carrito = models.IntegerField(primary_key=True)
    Identificacion_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ID_Domiciliario = models.ForeignKey(Domiciliario, on_delete=models.CASCADE)

admin.site.register(Carrito_de_Compra)
