'''
Realizar una función llamada año_bisiesto:
✓ Recibirá un año por parámetro
✓ Imprimirá “El año año es bisiesto” si el año es bisiesto
✓ Imprimirá “El año año no es bisiesto” si el año no es bisiesto
✓ Si se ingresa algo que no sea número, debe indicar que se ingrese un número.
Información a tener en cuenta:
Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque 
los múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 
no es bisiesto, 2000 es bisiesto, 1Ā00 no es bisiesto.
'''
def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        print(f"El año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")

es_bisiesto(2012)
es_bisiesto(2010)
es_bisiesto(2000)
es_bisiesto(1000)
