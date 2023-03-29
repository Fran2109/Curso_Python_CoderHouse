from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

handler403 = 'MainApp.views.handler_403'
handler404 = 'MainApp.views.handler_404'
handler500 = 'MainApp.views.handler_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MainApp.urls')),
    path('UsersApp/', include('UsersApp.urls')),
    path('PostsApp/', include('PostsApp.urls')),
    path('MessagesApp/', include('MessagesApp.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)