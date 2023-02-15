import json


def existe_archivo(ruta = "DB.json"):
    try:
        with open(ruta, 'r') as file:
            return True
    except FileNotFoundError:
        return False

def leer_archivo(ruta = "DB.json"):
    if(existe_archivo(ruta)):
        with open(ruta, 'r') as file:
            return json.load(file)
    else:
        return {}
    
def escribir_archivo(DB, ruta = "DB.json"):
    with open(ruta, 'w') as file:
        json.dump(DB, file, indent=4)
        
def validar_contraseña(contrasenia):
    try:
        if(len(contrasenia) < 8):
            raise Exception("La contraseña debe tener minimo 8 caracteres")
        if(len(contrasenia) > 16):
            raise Exception("La contraseña debe tener maximo 16 caracteres")
        if(contrasenia.isalpha()):
            raise Exception("La contraseña debe tener al menos un numero")
        if(contrasenia.isnumeric()):
            raise Exception("La contraseña debe tener al menos una letra")
        if(contrasenia.islower()):
            raise Exception("La contraseña debe tener al menos una letra mayuscula")
        if(contrasenia.isupper()):
            raise Exception("La contraseña debe tener al menos una letra minuscula")
        return True, "Contraseña valida"
    except Exception as mensaje:
        return False, mensaje
    
def register(ruta = "DB.json"):
    DB = leer_archivo(ruta)
    nombre = input("Ingrese el nombre de usuario: ")
    while(nombre in DB):
        print("Ya existe un Usuario registrado con el mismo nombre")
        nombre = input("Ingrese el nombre de usuario: ")
    else:
        contrasenia = input("Ingrese la contraseña: ")
        estado, mensaje = validar_contraseña(contrasenia)
        while(not estado):
            print(mensaje)
            contrasenia = input("Ingrese la contraseña: ")
            estado, mensaje = validar_contraseña(contrasenia)
        else:
            print(mensaje)
            DB[nombre] = contrasenia
            escribir_archivo(DB, ruta)
            print("Usuario registrado con exito")

def login(ruta = "DB.json"):
    DB = leer_archivo(ruta)
    nombre = input("Ingrese el nombre de usuario: ")
    while(nombre not in DB):
        print("El nombre de Usuario no existe")
        nombre = input("Ingrese el nombre de usuario: ")
    else:
        contrasenia = input("Ingrese su contraseña: ")
        while(contrasenia != DB[nombre]):
            print("Contraseña incorrecta. Vuelva a intentarlo. Ingrese exit para abortar")
            contrasenia = input("Ingrese su contraseña: ")
            if(contrasenia == "exit"):
                break
        else:
            print("Logueado correctamente")
            
def imprimir_usuarios(ruta = "DB.json"):
    DB = leer_archivo(ruta)
    cantidad = 0
    for key in DB:
        cantidad += 1
        print(f"Usuario Nro {cantidad}: {key}")

def main_manejo_usuarios(ruta = "DB.json"):
    
    opcion = 0

    while opcion != 4:
        print("1. Ingresar un nuevo usuario.")
        print("2. Loguearse en el sistema")
        print("3. Mostrar usuarios")
        print("4. Salir")
        
        try:
            opcion = int(input("Ingrese su opcion "))
        except ValueError:
            print("No ha ingresado un numero")
            continue
        
        if(opcion == 1):
            register(ruta)
        elif(opcion == 2):
            login(ruta)
        elif(opcion == 3):
            imprimir_usuarios(ruta)
        elif(opcion == 4):
            print("Fin del programa")
        else:
            print("Ingreso una opcion valida ")