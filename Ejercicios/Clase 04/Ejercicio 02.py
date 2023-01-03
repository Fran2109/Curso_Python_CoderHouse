'''
Para aprobar un crédito, el cliente debe ser mayor de edad. 
Además, debe tener una antigüedad en el sistema financiero 
de mínimo 3 años y un ingreso mayor a 2500 dólares. En 
caso no tenga la antigüedad suficiente, su ingreso mensual 
debe ser como mínimo 4000 dólares. Si no cumple ninguna 
de las condiciones, no se aprueba el crédito
Datos iniciales
✔ edad = 15
✔ antigüedad = 10
✔ ingreso = 1500
'''

edad = 15
antiguedad = 10
ingreso = 1500

if(edad >= 18):
    if(antiguedad >= 3):
        if(ingreso >= 2500):
            print("Si es posible asignarle un prestamo")
        else:
            print("No es posible asignar un credito porque no tiene como minimo 2500 dolares de ingresos")
    elif(ingreso >= 4000):
        print("Si es posible asignarle un prestamo")
    else:
        print("No es posible asignar un credito porque no tiene como minimo 3 años de antiguedad")
else:
    print("No es posible asignar un credito porque no es mayor de edad")