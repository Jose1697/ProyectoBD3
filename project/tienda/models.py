from __future__ import unicode_literals
from django.db import models


class Cliente(models.Model):
    nombres = models.CharField(max_length=20, null=True)
    apellidos = models.CharField(max_length=20, null=True)

class  Movil(models.Model):
    modelo  = models.CharField(max_length=20, null=True)
    marca  = models.CharField(max_length=20, null=True)
    precio = models.IntegerField(null = True)
    stock  = models.IntegerField(null = True)


class Vendedor(models.Model):
    nombres = models.CharField(max_length=20, null=True)
    apellidos = models.CharField(max_length=20, null=True)



#BERNILLA SAD OLVIDALA XD
#gazaso