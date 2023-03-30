from django.contrib.auth.views import LogoutView
from django.urls import path
from UsersApp.views import (EditarPerfil, Login, ModificarContrasenia,
                            Registro, acercaDeMi, informacionPerfil)

# Defino el "namespace" de la aplicación con el nombre "UsersApp".
app_name = 'UsersApp'

urlpatterns = [
    # En la primera ruta se define la dirección "/login/" que llama a la vista "Login" mediante el método "as_view()".
    path('login/', Login.as_view(), name="Login"),
    # En la segunda ruta se define la dirección "/registro/" que llama a la vista "Registro" mediante el método "as_view()".
    path('registro/', Registro.as_view(), name="Registro"),
    # En la tercera ruta se define la dirección "/logout/" que llama a la vista "LogoutView" y utiliza el template "inicio.html".
    path('logout/', LogoutView.as_view(template_name="inicio.html"), name="Logout"),
    # En la cuarta ruta se define la dirección "/acercaDeMi" que llama a la vista "acercaDeMi".
    path('acercaDeMi', acercaDeMi, name = "AcercaDeMi"),
    # En la quinta ruta se define la dirección "/informacionPerfil" que llama a la vista "informacionPerfil".
    path('informacionPerfil', informacionPerfil, name = "InformacionPerfil"),
    # En la sexta ruta se define la dirección "/editarPerfil" que llama a la vista "EditarPerfil" mediante el método "as_view()".
    path('editarPerfil', EditarPerfil.as_view(), name = 'EditarPerfil'),
    # En la séptima ruta se define la dirección "/modificarContrasenia" que llama a la vista "ModificarContrasenia" mediante el método "as_view()".
    path('modificarContrasenia', ModificarContrasenia.as_view(), name = 'ModificarContrasenia'),
]