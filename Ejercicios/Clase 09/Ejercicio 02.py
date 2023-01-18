'''
Escribir una función que reciba una muestra de números en 
una lista y devuelva su media.
'''

def media_de_lista(listaNumeros):
    return sum(listaNumeros) / len(listaNumeros)

media = media_de_lista([1, 2, 3, 4, 5, 6])

print(f"El promedio es {media}")