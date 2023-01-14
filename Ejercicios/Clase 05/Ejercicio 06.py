'''
Escribe un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los 
números y realiza una media aritmética.
'''

cantidad = int(input("Ingrese la cantidad: "))
suma = 0
for number in range(cantidad):
    number = int(input("Ingrese un numero: "))
    suma += number
else: 
    print(f"El resultado de la suma es {suma}")