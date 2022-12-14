cadena = "acitametaM ,5.8 ,otipeP ordeP"

cadena_volteada = cadena[::-1]

nombre_alumno = cadena_volteada[0:12]

print("Nombre:", nombre_alumno)

nota = cadena_volteada[14:17]

print("Nota:", nota)

materia = cadena_volteada[19:len(cadena_volteada)]

print("Materia:", materia)

cadena_formateada = nombre_alumno + " ha sacado un " + nota + " en " + materia

print(cadena_formateada)