from django.contrib.auth.views import LogoutView
from django.urls import path
from PostsApp.views import ListaMisPosts, PostDetalleMio

app_name = 'PostsApp'

urlpatterns = [
    path('listaMisPosts/', ListaMisPosts.as_view(), name="ListaMisPosts"),
    path('postDetalleMio/<int:pk>/', PostDetalleMio.as_view(), name="PostDetalleMio"),
]