'''
En una lista encontraremos diferentes 
operaciones lógicas. Calcular mentalmente 
el resultado de cada expresión y 
almacenarlo en una nueva lista la cual 
contendrá únicamente valores lógicos True y 
False. 
'''

expresiones = [
    not False,
    not 3 == 5,
    33/3 == 11 and 5 > 2,
    True or False,
    True*5 == 2.5*2 or 123 >= 23,
    12 > 7 and True < False
]

print("Resultado de not False =>", expresiones[0])
print("Resultado de not 3 == 5 =>", expresiones[1])
print("Resultado de 33/3 == 11 and 5 > 2 =>", expresiones[2])
print("Resultado de True or False =>", expresiones[3])
print("Resultado de True*5 == 2.5*2 or 123 >= 23 =>", expresiones[4])
print("Resultado de 12 > 7 and True < False =>", expresiones[5])