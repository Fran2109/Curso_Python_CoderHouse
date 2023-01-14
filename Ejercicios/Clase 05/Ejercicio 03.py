'''
Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un 
menú:
✓ Mostrar una suma de los dos números
✓ Mostrar una resta de los dos números (el primero menos el segundo)
✓ Mostrar una multiplicación de los dos números
✓ Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
✓ En caso de no introducir una opción válida, el programa informará de que no es correcta.
'''

respuesta = 0

numero1 = int(input("Ingrese el primer Numero "))
numero2 = int(input("Ingrese el segundo Numero "))
    
while(respuesta != 4):
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. Salir")
    respuesta = int(input("Elija una opción: "))
    if(respuesta == 1):
        print(f"El resultado de la suma es {numero1 + numero2}")
    elif(respuesta == 2):
        print(f"El resultado de la resta es {numero1 - numero2}")
    elif(respuesta == 3):
        print(f"El resultado de la multiplicacion es {numero1 * numero2}")
    elif(respuesta == 4):
        print("Salir")
    else:
        print("Opción no válida")
else:
    print("Fin del programa")
    
