from django.contrib.auth.views import LogoutView
from django.urls import path
from UsersApp.views import login_request, registro, acercaDeMi

app_name = 'UsersApp'

urlpatterns = [
    path('login/', login_request, name="Login"),
    path('registro/', registro, name="Registro"),
    path('logout/', LogoutView.as_view(template_name="inicio.html"), name="Logout"),
    path('acercaDeMi', acercaDeMi, name = "AcercaDeMi")
]