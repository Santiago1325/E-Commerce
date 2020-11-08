from django.db import models
from django.contrib import admin
# Create your models here.
class Plataforma(models.Model):
    ID_Plataforma = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=45)

admin.site.register(Plataforma)
