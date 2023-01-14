'''
Utilizando todo lo que sabes sobre cadenas, listas y sus 
métodos internos, transforma este texto:
gordon lanzó su curva&strawberry ha fallado por un pie!\n
-gritó Joe Castiglione&dos pies -le corrigió\n
Troop&strawberry menea la cabeza como disgustado...\n
-agrega el comentarista

Transforma el texto en:
Gordon lanzó su curva...
- Strawberry ha fallado por un pie! -gritó Joe Castiglione.
- Dos pies le corrigió Troop.
- Strawberry menea la cabeza como disgustado... -agrega el 
comentarista.
Lo único prohibido es modificar directamente el texto
ACTIVIDAD EN CLASE

'''

textoOriginal = "gordon lanzó su curva&strawberry ha fallado por un pie!\n-gritó Joe Castiglione&dos pies -le corrigió\nTroop&strawberry menea la cabeza como disgustado...\n-agrega el comentarista"

counter = 0
for oracion in textoOriginal.split("\n"):
    counter+=1
    if(counter == 1):
        oracion = oracion.capitalize()
        
    print(oracion)
