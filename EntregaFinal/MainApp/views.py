from django.shortcuts import render


# Vista del inicio del sitio
def inicio(request):
    return render(request, 'inicio.html')