from django.db import models
from apps.Domiciliario.models import Domiciliario
from apps.Direccion.models import Direccion
from django.contrib import admin
# Create your models here.


class Entrega(models.Model):
    ID_Entrega = models.IntegerField(primary_key=True)
    Fecha = models.DateField()
    ID_Domiciliario = models.ForeignKey(Domiciliario, on_delete=models.CASCADE)
    ID_Direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

admin.site.register(Entrega)
