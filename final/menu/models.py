from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Menu(models.Model):
    nombre=models.CharField(max_length=200)
    descripcion=models.TextField()
    costo_puntada=models.FloatField()

    def __str__(self):
        return self.nombre