from django.contrib.auth.models import User
from django.db import models


# Defino una clase llamada Profile, la cual hereda de la clase models.Model.
# Esta clase va a servir como modelo para el perfil de usuario.
class Profile(models.Model):
    # user: es un objeto OneToOneField que se relaciona con la clase User de Django, es decir, que representa un usuario.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # avatar: es un objeto ImageField que permite subir imágenes al servidor, y se guarda en la carpeta 'avatares/'.
    # Este campo puede ser nulo (null=True) y no es obligatorio (blank=True).
    avatar = models.ImageField(upload_to='avatares/', null=True, blank = True)
    # link: es un objeto URLField que permite guardar una URL en formato de cadena de texto.
    # Este campo puede ser nulo (null=True) y no es obligatorio (blank=True).
    link = models.URLField(blank=True)
    
    # Defino un método __str__ que devuelve una cadena de texto representando al objeto Profile, donde se muestra el nombre de usuario (self.user) y la ruta de la imagen de avatar (self.avatar).
    def __str__(self):
        return f"{self.user} - {self.avatar}"