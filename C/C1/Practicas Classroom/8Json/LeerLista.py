import json


with open('C/C1/Practicas Classroom/8Json/lista.json','r') as archivo:
    lista=json.load(archivo)

if not archivo.closed:
    print('Cerrando archivo...')
    archivo.close()

for elem in lista:
    print(elem, end=', ')