import json

midic={1:"Lapiz", 2:"Borrador", 3:"Cuaderno", 4:"Lapicero", "valor":2500}

with open('C/C1/Practicas Classroom/8Json/diccionario.json','w') as archivo:
    json.dump(midic, archivo)

if not archivo.closed:
    print('Cerrando archivo...')
    archivo.close()