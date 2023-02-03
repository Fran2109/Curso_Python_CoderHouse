'''
Crear una clase llamada Alumno, que posea como atributos de instancia el nombre y la nota del 
estudiante. Como métodos propios de la clase, se deberán definir correspondientemente el 
constructor, el método imprimir y resultado. 
Aclaración: Tanto los atributos como métodos, son de tipo públicos.
Importante: En la siguiente actividad en clase, implementaremos nuestro Diagrama de Clase, 
directamente en Python.
'''

class Alumno: 
    def __init__(self, nombre, nota): 
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print(f"El alumno {self.nombre} tiene una nota de {self.nota}")
    
    def resultado(self):
        if(self.nota >= 7):
            print(f"El alumno {self.nombre} aprobo")
        else:
            print(f"El alumno {self.nombre} desaprobo")

nuevoAlumno = Alumno("Francisco", 10)

nuevoAlumno.imprimir()

nuevoAlumno.resultado()