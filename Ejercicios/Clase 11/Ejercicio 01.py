'''
En la función de nuestro ejercicio hay un fallo potencial, averigua cuándo sucede y 
retorna el valor None en ese caso especial, en cualquier otro caso devuelve el 
resultado normal de la función.
>>> def dividir(a, b):
return a/b
Pista: Valor indeterminado
'''

def dividir(a = 0, b = 0):
    try:
        c = a/b
        return
    except Exception:
        return "NONE"

print(dividir())