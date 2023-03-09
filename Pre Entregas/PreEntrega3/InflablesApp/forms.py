from django import forms


class InflableFormulario(forms.Form):
    nombre = forms.CharField()
    alto = forms.FloatField(min_value=1, max_value=20)
    ancho = forms.FloatField(min_value=1, max_value=20)
    largo = forms.FloatField(min_value=1, max_value=20)
    
class JuegoFormulario(forms.Form):
    nombre = forms.CharField()
    cant_personas = forms.IntegerField(min_value=1, max_value=6)
    ancho = forms.FloatField(min_value=1, max_value=20)
    largo = forms.FloatField(min_value=1, max_value=20)