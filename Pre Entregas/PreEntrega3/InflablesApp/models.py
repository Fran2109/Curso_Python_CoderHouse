from django.db import models


class Inflable(models.Model):
    nombre = models.CharField(max_length=50)
    alto = models.FloatField()
    ancho = models.FloatField()
    largo = models.FloatField()