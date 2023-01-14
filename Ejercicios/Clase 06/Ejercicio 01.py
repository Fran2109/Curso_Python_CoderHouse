'''
Trabajaremos con el notebook de la sesión, específicamente sobre la 
temática de Sets. 
Crear un conjunto en Python que posea los siguientes elementos: 
✔ Colores: Rojo, Blanco, Azul.
✔ Posteriormente, agrega nuestro set de colores, los valores de: 
Violeta y Dorado
✔ Elimina a los colores: Celeste, Blanco y Dorado
Pregunta: ¿Qué pasa si queremos eliminar el color Celeste utilizando el 
método discard?
'''

colores = set(["Rojo", "Blanco", "Azul"])

print(colores)

colores.add("Violeta")
colores.add("Dorado")

print(colores)

colores.discard("Celeste")
colores.discard("Blanco")
colores.discard("Dorado")

print(colores)