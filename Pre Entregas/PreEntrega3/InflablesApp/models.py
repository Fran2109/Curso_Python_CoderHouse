from django.db import models


class Inflable(models.Model):
    nombre = models.CharField(max_length=50)
    alto = models.FloatField()
    ancho = models.FloatField()
    largo = models.FloatField()

class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    cant_personas = models.PositiveIntegerField()
    ancho = models.FloatField()
    largo = models.FloatField()
    
class Reserva(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    nombre_cliente = models.CharField(max_length=50)
    elemento = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)