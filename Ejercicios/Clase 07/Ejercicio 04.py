'''
A partir de una lista realizar las siguientes tareas sin modificar la lista original:
1. Borrar los elementos duplicados
2. Ordenar la lista de mayor a menor
3. Eliminar todos los números impares (  for ---- if (%2==1) ---- pop, remove   )
4. Realizar una suma de todos los números que quedan (sum(lista))
5. Añadir como primer elemento de la lista la suma realizada insert(0, suma)
6. Devolver la lista modificada
7. Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a 
partir del segundo, concuerda con el primer número de la lista
'''

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

sinDuplicar = []
for item in lista:
    if(not item in sinDuplicar):
        sinDuplicar.append(item)

print(f"1. {sinDuplicar}")

ordenada = lista
ordenada.sort(reverse=True)

print(f"2. {ordenada}")

listaPar = []
for item in lista:
    if(item%2 == 0):
        listaPar.append(item)
        
print(f"3. {listaPar}")

print(f"4. {sum(lista)}")

listaPar.insert(0, sum(lista))

print(f"5. {listaPar}")