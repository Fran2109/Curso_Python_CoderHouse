# Importo el módulo 'path' de Django desde el módulo 'django.urls'.
from django.urls import path
# Importo todas las vistas de la aplicación 'MessagesApp' desde el módulo 'MessagesApp.views'.
from MessagesApp.views import *

# Defino el nombre de la aplicación como 'MessagesApp'.
app_name = 'MessagesApp'

urlpatterns = [
    # Esta ruta de URL se utiliza para mostrar una lista de mensajes en la aplicación.
    path('listaMensajes/', ListaMensajes.as_view(), name="ListaMensajes"),
]