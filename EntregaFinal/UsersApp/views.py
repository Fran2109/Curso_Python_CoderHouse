from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from UsersApp.forms import FormularioRegistro


# Create your views here.
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("MainApp:Inicio")
            else:
                return render(request, 'login.html', {"form": form})
        else:
            return render(request, 'login.html', {"form": form})
    form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})

            
    
def registro(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("MainApp:Inicio")
    else:
        form = FormularioRegistro()
    return render(request, 'registro.html', {"form": form})