'''
Un curso se ha dividido en dos grupos diferentes: A y B de 
acuerdo al nombre y a una preferencia (Marvel o Capcom). 
El grupo A está formado por fans de Marvel con un nombre 
anterior a la M y los fans de Capcom con un nombre 
posterior a la N y el grupo B por el resto. Escribir un 
programa que pregunte al usuario su nombre y preferencia, 
y muestre por pantalla el grupo que le corresponde.
Ej.:
¿Cómo te llamas? Alan
¿Cuál es tu preferencia (M o C)? C
Tu grupo es B
Para preguntarle al usuario, recuerda usar input.
'''

nombre = input("Ingrese su nombre: ")
preferencia = input("Ingrese su preferencia (M o C): ")

if (nombre[0] < "M" and preferencia == "M") or (nombre[0] > "N" and preferencia == "C"):
  print("Grupo A")
else:
  print("Grupo B")