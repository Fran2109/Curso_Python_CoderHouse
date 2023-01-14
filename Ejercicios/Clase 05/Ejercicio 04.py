'''
Escribe un programa que lea un número impar por teclado. Si el usuario no introduce un número 
impar, debe repetirse el proceso hasta que lo introduzca correctamente.
'''

numero = int(input("Ingrese un numero "))

while(numero % 2 == 0):
    print("El numero ingresado no es impar")
    numero = int(input("Ingrese un numero "))
else:
    print("El numero ingresado es impar")