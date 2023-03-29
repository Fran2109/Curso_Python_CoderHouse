from django.db import models
from UsersApp.models import Profile

class Mensaje(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} -> {self.fecha_creacion}"
