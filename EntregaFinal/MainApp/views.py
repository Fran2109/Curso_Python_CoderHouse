from django.shortcuts import render


# Esta función recibe una petición HTTP y renderiza la plantilla 'inicio.html', que muestra la página de inicio del sitio.
def inicio(request):
    return render(request, 'inicio.html')

# Esta función maneja los errores de acceso denegado (HTTP 403) y renderiza la plantilla '403.html'.
def handler_403(request, exception):
    return render(request, '403.html', {}, status=403)

# Esta función maneja los errores de página no encontrada (HTTP 404) y renderiza la plantilla '404.html', pasando el objeto de excepción como contexto para proporcionar más información sobre el error.
def handler_404(request, exception):
    return render(request, '404.html', {'exception': exception}, status=404)

# Esta función maneja los errores de error interno del servidor (HTTP 500) y renderiza la plantilla '500.html'.
def handler_500(request):
    return render(request, '500.html', {}, status=500)