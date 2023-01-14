'''
Deberás crear un diccionario que almacene a los ganadores de la Copa Mundial de 
la FIFA desde el año 1990 al 2018. Y mostrarlo por pantalla.
'''

winners = {1990: 'Alemania', 1994: 'Brasil', 1998: 'Francia', 2002: 'Brasil', 2006: 'Italia', 2010: 'España', 2014: 'Alemania', 2018: 'Francia' }

for key in winners:
    print(f"El ganador del año {key} es {winners[key]}")