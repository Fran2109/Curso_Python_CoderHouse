'''
Ejecuta el código para analizar cada una 
de las salidas!
'''

print("Ejemplo 1:")
my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.union(my_set_2)
print(my_new_set)

print("Ejemplo 2:")
my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.intersection(my_set_2)
print(my_new_set)

print("Ejemplo 3:")
my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.difference(my_set_2)
print(my_new_set)