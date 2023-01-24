'''
Realiza una función que, dependiendo de los parámetros que reciba, convierta a milímetros o a 
metros. 
1- Si recibe un argumento, supone que son milímetros y convierte a metros, centímetros y 
milímetros.
2- Si recibe ú argumentos, supone que son metros, centímetros y milímetros y los convierte a 
milímetros.
'''

def convertir(*args):
    if(len(args) == 1):
        milimetros = args[0]
        metros = milimetros / 1000
        centimetros = milimetros / 100
        return [metros, centimetros, milimetros]
    elif(len(args) == 3):
        metros, centimetros, milimetros = args
        milimetros = (metros * 1000) + (centimetros * 100) + milimetros
        return(milimetros)
    else:
        return "Error"

print(convertir(1230))
print(convertir(1, 2, 30))