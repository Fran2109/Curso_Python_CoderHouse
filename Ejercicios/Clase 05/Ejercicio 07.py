'''
Escribe un programa que pida al usuario un número entero del 0 al 9, y que mientras el número 
no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista 
de números y notificarlo:
🖐 Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una 
lista (devuelve True o False).
'''

numero = int(input("Ingrese un numero del 0 al 9: "))

while(numero < 0 or numero > 9):
    numero = int(input("Ingrese un numero del 0 al 9: "))
else:
    if(numero in [2, 4, 6]):
        print("Es un numero valido")
    else:
        print("Es un numero no valido")