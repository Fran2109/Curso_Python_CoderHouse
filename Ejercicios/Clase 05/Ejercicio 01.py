'''
Calcular la suma de una cantidad de números enteros 
ingresados por el usuario directamente utilizando la 
función input (). 
Para  finalizar  la  ejecución  del  programa,  el  usuario 
debe  escribir  la  palabra  exit().  El  programa  debe 
validar dicha acción. 
Finalmente, el algoritmo debe mostrar la suma parcial 
y total obtenida.
'''

respuesta = input("Ingrese un numero para sumar o exit() para salir ")

suma = 0
cant = 0

while not respuesta == "exit":
    suma += int(respuesta)
    cant += 1
    respuesta = input("Ingrese un numero para sumar o exit() para salir ")
else:
    if(cant > 0):
        print(f"La suma total es {suma} y la parcial es {suma/cant}")
    else:
        print(f"La suma total es {suma}")