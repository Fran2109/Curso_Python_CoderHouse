'''
Escribir un programa que le solicite al usuario su nombre, edad, dirección y que, posteriormente, lo 
muestre por pantalla:
Ejemplo del output solicitado: 
✓ Juan tiene 25 años, y vive en Carrera 7 - Bogotá
'''

persona = dict()

persona["Nombre"] = input("Ingrese su nombre: ")

persona["Edad"] = int(input("Ingrese su edad: "))

persona["Direccion"] = input("Ingrese su direccion: ")

print(f"{persona['Nombre']} tiene {persona['Edad']} años, y vive en {persona['Direccion']}")