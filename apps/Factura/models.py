from django.db import models
from apps.Carrito_de_Compra.models import Carrito_de_Compra
from apps.Videojuego.models import Videojuego
from django.contrib import admin
# Create your models here.



class Factura(models.Model):
    ID_Factura = models.IntegerField(primary_key=True)
    Valor_Total = models.IntegerField()
    Metodo_De_Pago = models.CharField(max_length=45)
    ID_Carrito_Carrito_De_Compras = models.ForeignKey(Carrito_de_Compra, on_delete=models.CASCADE)
    Codigo_Video_Juegos = models.ForeignKey(Videojuego, on_delete=models.CASCADE)

admin.site.register(Factura)
