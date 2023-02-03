'''
Tomando la solución del ejercicio anterior, en lugar de devolver None al dividir entre cero, tienes 
que capturar una excepción que muestre por pantalla EXACTAMENTE el mensaje: “No se puede 
dividir entre cero”; si falla el código
>>> def dividir(a, b):
if b == 0:
         return None
return a/b
'''

def dividir(a = 0, b = 0):
    try:
        c = a/b
        return c
    except TypeError:
        return("No se puede dividir entre variables que no sean numeros")
    except ZeroDivisionError:
        return("No se puede dividir entre cero")

print(dividir())