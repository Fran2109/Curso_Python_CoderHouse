class Persona:
    # Constructor de la Clase Persona
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    # Metodo STR para poder imprimir una Persona
    def __str__(self):
        return f"Objeto del tipo: {type(self).__name__}\nAtributos\n* Nombre: {self.nombre}\n* Apellido: {self.apellido}\n* Edad: {self.edad}"
    
class Cliente(Persona):
    # Constructor de la Clase Cliente que hereda de la Clase Person
    def __init__(self, nombre, apellido, edad, gastado, mail, gustos):
        super().__init__(nombre, apellido, edad)
        self.gastado = gastado
        self.mail = mail
        self.gustos = gustos
    
    # Metodo STR para poder imprimir un Cliente que hereda de Persona y le agrega las propiedades extra
    def __str__(self):
        mensaje = f"{super().__str__()}\n* Gastado: {self.gastado}\n* Mail: {self.mail}"
        mensaje += "\n* Gustos:"
        for gusto in self.gustos:
            mensaje+=f"\n  - {gusto}"
        return mensaje
    
    # Metodo para registrar un gasto. Se valida que el monto sea valido
    def compra(self, gastoExtra):
        if(type(gastoExtra).__name__ != "int" and type(gastoExtra).__name__ != "float"):
            print("El gasto extra no es un numero")
        elif(gastoExtra<=0):
            print("El gasto extra no puede ser negativo")
        else:
            self.gastado += gastoExtra
            print(f"Se ha registrado un gasto de {gastoExtra}")
            print(f"El total gastado de {self.nombre} {self.apellido} es {self.gastado}")

    # Metodo para enviar un mail al cliente
    def enviar_mail(self, mensaje):
        print(f"Se envio el mensaje '{mensaje}' al mail {self.mail}")

    # Metodo para validar si un gusto esta en la lista de gustos del cliente
    def validar_gusto(self, gusto):
        if(gusto in self.gustos):
            print(f"{self.nombre} {self.apellido} si tiene gusto por: {gusto}")
        else:
            print(f"{self.nombre} {self.apellido} no tiene gusto por: {gusto}")
    
    # Metodo para agregar un gusto a la lista de gustos del cliente
    def agregar_gusto(self, gusto):
        if(gusto in self.gustos):
            print(f"{self.nombre} {self.apellido} ya posee gusto por: {gusto}")
        else:
            self.gustos.append(gusto)
            print(f"{self.nombre} {self.apellido} ahora posee gusto por: {gusto}")
    
    # Metodo para quitar un gusto a la lista de gustos del cliente
    def quitar_gusto(self, gusto):
        if(gusto not in self.gustos):
            print(f"{self.nombre} {self.apellido} no posee gusto por: {gusto}")
        else:
            self.gustos.remove(gusto)            
            print(f"{self.nombre} {self.apellido} ya no posee gusto por: {gusto}")