from django.contrib.auth.views import LogoutView
from django.urls import path
from UsersApp.views import (EditarPerfil, Login, ModificarContrasenia,
                            Registro, acercaDeMi, informacionPerfil)

app_name = 'UsersApp'

urlpatterns = [
    path('login/', Login.as_view(), name="Login"),
    path('registro/', Registro.as_view(), name="Registro"),
    path('logout/', LogoutView.as_view(template_name="inicio.html"), name="Logout"),
    path('acercaDeMi', acercaDeMi, name = "AcercaDeMi"),
    path('informacionPerfil', informacionPerfil, name = "InformacionPerfil"),
    path('editarPerfil', EditarPerfil.as_view(), name = 'EditarPerfil'),
    path('modificarContrasenia', ModificarContrasenia.as_view(), name = 'ModificarContrasenia'),
]