import json

with open('C/C1/Practicas Classroom/8Json/lista.json'
          ,'r')as archivo:#abro el archivo y lo guardo en
    #archivo
    lista=json.load(archivo)#leo el archivo internamente

if not archivo.closed:#si el archivo no está cerrrado lo cierro
    print('Cerrando archivo...')
    archivo.close()

for elem in lista:
    print(elem, end=', ')#leo cada elemento en la lista