from django.db import models
from django.contrib import admin
# Create your models here.

class Franquicia(models.Model):
    ID_Franquicia = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=45)

admin.site.register(Franquicia)
