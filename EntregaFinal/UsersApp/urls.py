from django.urls import path
from UsersApp.views import registro

app_name = 'UsersApp'

urlpatterns = [
    path('registro/', registro, name="Registro"),
]