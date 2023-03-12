from django import forms


# Formulario para los Inflables
class InflableFormulario(forms.Form):
    nombre = forms.CharField()
    alto = forms.FloatField(min_value=1, max_value=20)
    ancho = forms.FloatField(min_value=1, max_value=20)
    largo = forms.FloatField(min_value=1, max_value=20)
    
# Formulario para los Juegos
class JuegoFormulario(forms.Form):
    nombre = forms.CharField()
    cant_personas = forms.IntegerField(min_value=1, max_value=6)
    ancho = forms.FloatField(min_value=1, max_value=20)
    largo = forms.FloatField(min_value=1, max_value=20)

# Input para la fecha
class DateInput(forms.DateInput):
    input_type = 'date'

# Input para la hora
class TimeInput(forms.TimeInput):
    input_type = 'time'
  
# Formulario para las reservas  
class ReservaFormulario(forms.Form):
    fecha = forms.DateField(widget=DateInput)
    hora_inicio = forms.TimeField(widget=TimeInput)
    hora_fin = forms.TimeField(widget=TimeInput)
    nombre_cliente = forms.CharField(max_length=50)
    elemento = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)