from django.shortcuts import render


# Vista del inicio del sitio
def inicio(request):
    return render(request, 'inicio.html')

def handler_403(request, exception):
    return render(request, '403.html', {}, status=403)

def handler_404(request, exception):
    return render(request, '404.html', {'exception': exception}, status=404)

def handler_500(request):
    return render(request, '500.html', {}, status=500)