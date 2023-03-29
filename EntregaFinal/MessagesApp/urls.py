from django.urls import path
from MessagesApp.views import *

app_name = 'MessagesApp'

urlpatterns = [
    path('listaMensajes/', ListaMensajes.as_view(), name="ListaMensajes"),
]