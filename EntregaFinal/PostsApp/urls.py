from django.contrib.auth.views import LogoutView
from django.urls import path
from PostsApp.views import ListaMisPosts, PostDetalle

app_name = 'PostsApp'

urlpatterns = [
    path('listaMisPosts/', ListaMisPosts.as_view(), name="ListaMisPosts"),
    path('listaPosts/<int:pk>/', PostDetalle.as_view(), name="PostDetalle"),
]