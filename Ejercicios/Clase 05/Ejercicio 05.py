'''
Escribe un programa que sume todos los números enteros impares desde el 0 hasta el 100:
🖐 Ayuda: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer parámetro en 
la función range(inicio, fin, salto) indica un salto de números.
'''

respuesta = 0

for number in range(1, 100, 2):
    respuesta += number
else: 
    print(f"La suma es {respuesta}")