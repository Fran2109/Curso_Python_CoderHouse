print("Promedio de Equipo")

ganados = int(input("Cantidad de partidos ganados: "))
empatados = int(input("Cantidad de partidos empatados: "))
perdidos = int(input("Cantidad de partidos perdidos: "))

promedio = (ganados * 3 + empatados * 1 + perdidos * 0) / (ganados + empatados + perdidos)

print("Promedio final: ",promedio)