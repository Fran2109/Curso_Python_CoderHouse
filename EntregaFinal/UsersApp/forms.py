from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class FormularioLogin(AuthenticationForm):
    username = forms.CharField(label = "Nombre de Usuario", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    class Meta:
        model = User
        fields = ('username', 'password')
        help_texts = {k:"" for k in fields}
    
class FormularioRegistro(UserCreationForm):
    username = forms.CharField(label = "Nombre de Usuario", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.CharField(label="Email", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}