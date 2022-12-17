
lista1 = ["Primer Lista", 543564]

print("Lista 1:", lista1)

lista1.append(456789)
lista1.append("Hola Mundo")

print("Lista 1:", lista1)

lista2 = ["Segunda Lista", 5432]

print("Lista 2:", lista2)

lista2.append("Hola y Adios")
lista2.append(5555)

print("Lista 2:", lista2)

lista3 = lista1[0:len(lista1)-1]

print("Lista 3:", lista3)

lista4 = lista2[1:len(lista2)-1]

print("Lista 4:", lista4)

lista5 = lista3 + lista4

print("Lista 5:", lista5)