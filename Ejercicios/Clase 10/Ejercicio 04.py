'''
Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:
✓ Si el primer número es mayor que el segundo, debe devolver 1.
✓ Si el primer número es menor que el segundo, debe devolver -1.
✓ Si ambos números son iguales, debe devolver un 0.
'''

def relacion(numero1, numero2):
    if(numero1 > numero2): 
        return 1
    elif(numero2 > numero1):
        return -1
    else:
        return 0
    
print(relacion(5, 10))
print(relacion(10, 5))
print(relacion(5, 5))