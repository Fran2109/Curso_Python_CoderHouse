'''
Desafío de tuplas
Descripción de la actividad. 
A partir de una variable llamada tupla, imprimir por pantalla de forma ordenada, lo siguiente:
1. El último ítem de tupla
2. El número de ítems de tupla
3. La posición donde se encuentra el ítem 87 de tupla
4. Una lista con los últimos tres ítems de tupla
5. Un ítem que haya en la posición 8 de tupla
6. El número de veces que el ítem 7 aparece en tupla

Copia esta tupla para iniciar el ejercicio:
tupla = (8, 15, 4, 39, 5, 89, 87,  19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

'''
tupla = (8, 15, 4, 39, 5, 89, 87,  19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

print("1:", tupla[len(tupla)-1])

print("2:", len(tupla))

print("3:", tupla.index(87))

print("4:", list(tupla[len(tupla)-3:]))

print("5:", tupla[8])

print("6:", tupla.count(7))