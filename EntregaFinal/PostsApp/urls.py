from django.urls import path
# Importo todas las vistas definidas en el archivo views.py dentro de la misma aplicación PostsApp mediante el uso del asterisco (*).
from PostsApp.views import *

# Defino el nombre de la aplicación como 'PostsApp'.
app_name = 'PostsApp'

urlpatterns = [
    # 'listaMisPosts/' llama a la vista 'ListaMisPosts' y se le asigna el nombre 'ListaMisPosts'.
    path('listaMisPosts/', ListaMisPosts.as_view(), name="ListaMisPosts"),
    # 'ListaPosts/' llama a la vista 'ListaPosts' y se le asigna el nombre 'ListaPosts'.
    path('ListaPosts/', ListaPosts.as_view(), name="ListaPosts"),
    # 'postDetalleMio/int:pk/' llama a la vista 'PostDetalleMio' y se le asigna el nombre 'PostDetalleMio', donde int:pk es un parámetro que indica que se espera un número entero que se utilizará como identificador de un post.
    path('postDetalleMio/<int:pk>/', PostDetalleMio.as_view(), name="PostDetalleMio"),
    # 'postDetalle/int:pk/' llama a la vista 'PostDetalle' y se le asigna el nombre 'PostDetalle', donde int:pk es un parámetro que indica que se espera un número entero que se utilizará como identificador de un post.
    path('postDetalle/<int:pk>/', PostDetalle.as_view(), name="PostDetalle"),
    # 'postBorrado/int:pk/' llama a la vista 'PostBorrado' y se le asigna el nombre 'PostBorrado', donde int:pk es un parámetro que indica que se espera un número entero que se utilizará como identificador de un post.
    path('postBorrado/<int:pk>/', PostBorrado.as_view(), name='PostBorrado'),
    # 'postCreacion/' llama a la vista 'PostCreacion' y se le asigna el nombre 'PostCreacion'.
    path('postCreacion/', PostCreacion.as_view(), name="PostCreacion"),
    # 'postEdicion/int:pk' llama a la vista 'PostEdicion' y se le asigna el nombre 'PostEdicion', donde int:pk es un parámetro que indica que se espera un número entero que se utilizará como identificador de un post.
    path('postEdicion/<int:pk>', PostEdicion.as_view(), name="PostEdicion"),
    # 'postBusqueda' llama a la vista 'busquedaPosts' y se le asigna el nombre 'BusquedaPosts'.
    path('postBusqueda', busquedaPosts, name="BusquedaPosts")
]