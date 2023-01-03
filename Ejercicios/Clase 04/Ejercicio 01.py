'''
Escribir un programa que indique la generación 
correspondiente para un año de nacimiento indicado.
Importante: Para los años que no pertenezcan a ninguna 
generación, se deberá colocar: “No existe generación 
asociada”
'''

anioDeNacimiento = int(input("Ingrese su año de nacimiento "))

if(1920 <= anioDeNacimiento and anioDeNacimiento <= 1940):
    print("Pertenece a la Generacion Silenciosa")
elif(1946 <= anioDeNacimiento and anioDeNacimiento <= 1964):
    print("Pertenece a la Baby Boomer")
elif(1965 <= anioDeNacimiento and anioDeNacimiento <= 1979):
    print("Pertenece a la Generacion X")
elif(1980 <= anioDeNacimiento and anioDeNacimiento <= 2000):
    print("Pertenece a la Generacion Y")
elif(2001 <= anioDeNacimiento and anioDeNacimiento <= 2010):
    print("Pertenece a la Generacion Z")
else:
    print("No existe generacion asociada")