'''
Escribir un programa que guarde en una variable en un diccionario 
{'Dolar':'$','Euro':'€', 'Libra':'£'}. 
Luego se le deberá solicitar al usuario que ingrese la divisa que desea 
visualizar. 
En el caso de ingresar una divisa no existente en nuestro diccionario, 
deberemos indicarle con un mensaje de notificación que la divisa no se 
encuentra disponible.
'''

divisas = {'Dolar':'$','Euro':'€', 'Libra':'£'}

print(divisas)

divisa = input("Ingrese la divisa que desea visualizar: ")

if(divisa in divisas.keys()):
    print("La divisa ya existe")
else: 
    simbolo = input("Ingrese el simbolo de la divisa: ")
    divisas[divisa] = simbolo

print(divisas)
