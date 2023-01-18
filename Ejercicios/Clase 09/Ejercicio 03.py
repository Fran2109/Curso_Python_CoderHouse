'''
Crea un programa que le pida dos números enteros al 
usuario y diga por consola, si alguno de ellos es múltiplo del 
otro. La función debe llamarse es_multiplo().
'''

def es_multiplo(numero1, numero2):
    return numero1 % numero2 == 0 or numero2 % numero1 == 0

numero1 = int(input("Ingrese un número entero: "))
numero2 = int(input("Ingrese otro numero entero: "))

print(f"Es Multiplo? {es_multiplo(numero1, numero2)}")