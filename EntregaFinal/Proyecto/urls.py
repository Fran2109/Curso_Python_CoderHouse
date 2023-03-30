from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

handler403 = 'MainApp.views.handler_403'
handler404 = 'MainApp.views.handler_404'
handler500 = 'MainApp.views.handler_500'

urlpatterns = [
    # El primer patrón de URL es para la interfaz de administración del sitio web.
    path('admin/', admin.site.urls),
    # El segundo patrón de URL es para el módulo MainApp, que es la aplicación principal del sitio web.
    path('', include('MainApp.urls')),
    # Los siguientes patrones de URL son para las aplicaciones UsersApp, PostsApp y MessagesApp.
    path('UsersApp/', include('UsersApp.urls')),
    path('PostsApp/', include('PostsApp.urls')),
    path('MessagesApp/', include('MessagesApp.urls')),
]

# Utilizo la función += para agregar la URL estática del archivo multimedia a urlpatterns, que sirve para proporcionar acceso público a los archivos de medios cargados en la aplicación. Esto se hace a través de la variable MEDIA_URL y MEDIA_ROOT que se especifican en el archivo settings.py de la aplicación Django.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)