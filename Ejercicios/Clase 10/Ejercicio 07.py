'''
Realiza una función separar() que tome una lista de números enteros y devuelva dos listas 
ordenadas. La primera con los números pares, y la segunda con los números impares:
'''

def separar(*args):
    lista = list(args)
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

print(separar(2, 3, 4, 6, 8, 21, 10, 4, 6, 4, 65))