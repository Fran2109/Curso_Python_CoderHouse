# Importo la librería de Django para definir modelos
from django.db import models
# Importo el modelo Profile definido en la aplicación UsersApp.
from UsersApp.models import Profile


# Defino el modelo Post que hereda de models.Model, que es la clase base para definir modelos en Django:
class Post(models.Model):
    # Creo un campo de clave foránea que apunta al modelo Profile.
    # Si se borra el perfil del usuario, se borrarán también los posts que el usuario haya creado.
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # Creo un campo de texto que permite almacenar un título de máximo 255 caracteres.
    titulo = models.CharField(max_length=255)
    # Creo un campo de texto que permite almacenar un subtítulo de máximo 255 caracteres.
    subtitulo = models.CharField(max_length=255)
    # Creo un campo de texto que permite almacenar contenido del post sin límite de caracteres.
    contenido = models.TextField()
    # Creo un campo que almacena la fecha y hora de creación del post.
    # Se rellena automáticamente con la fecha y hora actual.
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    # Creo un campo que almacena la fecha y hora de la última modificación del post.
    # Se actualiza automáticamente cada vez que se modifica el post.
    fecha_modificacion = models.DateTimeField(auto_now=True)
    # Creo un campo que permite almacenar una imagen de fondo para el post.
    # La imagen se guarda en la carpeta fondo dentro del directorio media y es opcional.
    fondo = models.ImageField(upload_to='fondo/', null=True, blank = True)

    def __str__(self):
        # Defino el método __str__() que devuelve una representación en forma de cadena del objeto Post.En este caso, devuelve el título del post.
        return self.titulo
