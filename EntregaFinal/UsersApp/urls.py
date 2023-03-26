from django.contrib.auth.views import LogoutView
from django.urls import path
from UsersApp.views import (acercaDeMi, editarPerfil, informacionPerfil,
                            login_request, registro, modificarContrasenia)

app_name = 'UsersApp'

urlpatterns = [
    path('login/', login_request, name="Login"),
    path('registro/', registro, name="Registro"),
    path('logout/', LogoutView.as_view(template_name="inicio.html"), name="Logout"),
    path('acercaDeMi', acercaDeMi, name = "AcercaDeMi"),
    path('informacionPerfil', informacionPerfil, name = "InformacionPerfil"),
    path('editarPerfil', editarPerfil, name = 'EditarPerfil'),
    path('modificarContrasenia', modificarContrasenia, name = 'ModificarContrasenia'),
]