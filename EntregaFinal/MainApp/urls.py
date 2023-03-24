from django.urls import path
from MainApp.views import inicio

app_name = 'MainApp'

urlpatterns = [
    path('', inicio, name="inicio"),
]