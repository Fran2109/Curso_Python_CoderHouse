from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       UserChangeForm, UserCreationForm)
from django.contrib.auth.models import User
from UsersApp.models import Profile


class FormularioLogin(AuthenticationForm):
    username = forms.CharField(label = "Nombre de Usuario", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    class Meta:
        model = User
        fields = ('username', 'password')
        help_texts = {k:"" for k in fields}
    
class FormularioRegistro(UserCreationForm):
    username = forms.CharField(label = "Nombre de Usuario", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(label = "Nombre", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label = "Apellido", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.CharField(label="Email", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    link = forms.URLField(label="Link", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    avatar = forms.ImageField(label="Ingrese su Avatar", required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'link', 'avatar']
        help_texts = {k:"" for k in fields}
        
class FormularioEditarPerfil(UserChangeForm):
    username = forms.CharField(label = "Cambiar Nombre de Usuario", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(label = "Cambiar Nombre", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label = "Cambiar Apellido", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.CharField(label="Cambiar Email", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    password = None
    link = forms.URLField(label="Cambiar Link", required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    avatar = forms.ImageField(label="Ingrese su Avatar", required=False)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'link', 'avatar']
        help_texts = {k:"" for k in fields}
        
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            if("avatar" in self.cleaned_data and self.cleaned_data["avatar"] is not None):
                user.profile.avatar = self.cleaned_data["avatar"]
                user.profile.save()
            if("link" in self.cleaned_data and self.cleaned_data["link"] is not ""):
                user.profile.link = self.cleaned_data["link"]
                user.profile.save()
        return user
    
    
class FormularioEditarContrasenia(PasswordChangeForm):
    old_password = forms.CharField(label=("Contraseña Actual"), widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nueva Contraseña"), widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita Nueva Contraseña"), widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields}