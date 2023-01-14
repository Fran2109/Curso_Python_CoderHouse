'''
Utilizando todo lo que sabes sobre cadenas, listas y sus 
métodos internos, transforma este texto:
gordon lanzó su curva&strawberry ha fallado por un pie!\n
-gritó Joe Castiglione&dos pies -le corrigió\n
Troop&strawberry menea la cabeza como disgustado..\n
-agrega el comentarista

Transforma el texto en:
Gordon lanzó su curva...
- Strawberry ha fallado por un pie! -gritó Joe Castiglione.
- Dos pies le corrigió Troop.
- Strawberry menea la cabeza como disgustado... -agrega el comentarista.
Lo único prohibido es modificar directamente el texto

'''

textoOriginal = 'gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista'

counter = 0
for oracion in textoOriginal.split("&"):
    counter+=1
    if(counter == 1):
        oracion = oracion.capitalize() + "..."
    elif(counter == 2):
        oracion = "- " + oracion.capitalize()
        oracion = oracion.replace("joe castiglione", "Joe Castiglione.")
    elif(counter == 3):
        oracion = "- " + oracion.capitalize()
        oracion = oracion.replace("troop", "Troop.")
        oracion = oracion.replace("-le", "le")
    elif(counter == 4):
        oracion = oracion.capitalize()
        oracion = oracion.replace("..", "...")
        oracion = "- " + oracion + "."
    print(oracion)