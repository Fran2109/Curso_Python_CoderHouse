from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Urls para la aplicacion
    path('InflablesApp/', include('InflablesApp.urls'))
]
