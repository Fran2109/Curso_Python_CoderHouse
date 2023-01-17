'''
Crea un programa que pida por teclado (input) 
los datos de tus tres hobbies favoritos y los 
mismos se guarden en un archivo que se llame 
miHobbieFavorito.txt.
'''

ruta = "Ejercicios/Clase 08"

respuesta = input("¿Cuál es tu hobby favorito? ")

while(respuesta):
    f = open(ruta + "/Ejercicio 01.txt", "a")
    f.write(respuesta)
    f.close()
    respuesta = input("¿Cuál es tu hobby favorito? ")
else: 
    f = open(ruta + "/Ejercicio 01.txt", "r")
    print(f.read())
    f.close()