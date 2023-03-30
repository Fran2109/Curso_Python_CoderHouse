# Importo el módulo 'models' de Django y el modelo 'Profile' desde el módulo 'UsersApp.models'
from django.db import models
from UsersApp.models import Profile

# Defino un modelo 'Mensaje' que hereda de 'models.Model', que es la clase base de modelos de Django.
class Mensaje(models.Model):
    # Defino un campo 'author' que es una clave externa que hace referencia al modelo 'Profile'. Si se elimina un perfil, también se eliminarán todos los mensajes asociados a ese perfil.
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # Defino un campo 'contenido' que es un campo de texto que almacena el contenido del mensaje.
    contenido = models.TextField()
    # Defino un campo 'fecha_creacion' que es un campo de fecha y hora que registra la fecha y hora en que se creó el mensaje. Este campo se establece automáticamente en la fecha y hora actuales del sistema cuando se crea un nuevo mensaje.
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Defino un método '__str__' que devuelve una representación de cadena del objeto 'Mensaje'.
    def __str__(self):
        return f"{self.author} -> {self.contenido}"
