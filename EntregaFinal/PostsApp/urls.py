from django.urls import path
from PostsApp.views import *

app_name = 'PostsApp'

urlpatterns = [
    path('listaMisPosts/', ListaMisPosts.as_view(), name="ListaMisPosts"),
    path('ListaPosts/', ListaPosts.as_view(), name="ListaPosts"),
    path('postDetalleMio/<int:pk>/', PostDetalleMio.as_view(), name="PostDetalleMio"),
    path('postDetalle/<int:pk>/', PostDetalle.as_view(), name="PostDetalle"),
]