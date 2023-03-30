# Importo el módulo 'admin' de Django.contrib.
from django.contrib import admin
# Import el modelo 'Profile' desde el módulo 'MessagesApp.models'
from UsersApp.models import Profile
# Import el modelo 'Mensaje' desde el módulo 'MessagesApp.models'
from MessagesApp.models import Mensaje
# Import el modelo 'Post' desde el módulo 'MessagesApp.models'
from PostsApp.models import Post


# Registro el modelo "Mensaje" en mi panel de administración para que pueda ser visualizado y editado por los usuarios con los permisos adecuados.
admin.site.register(Mensaje)
# Registro el modelo "Profile" en mi panel de administración para que pueda ser visualizado y editado por los usuarios con los permisos adecuados.
admin.site.register(Profile)
# Registro el modelo "Post" en mi panel de administración para que pueda ser visualizado y editado por los usuarios con los permisos adecuados.
admin.site.register(Post)