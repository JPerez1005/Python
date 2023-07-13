import json

with open('C/C1/Practicas Classroom/8Json/diccionario.json'
          ,'r')as archivo:#abro el archivo y lo guardo en
    #archivo
    Diccionario=json.load(archivo)#leo el archivo internamente

if not archivo.closed:#si el archivo no está cerrrado lo cierro
    print('Cerrando archivo...')
    archivo.close()

with open('C/C1/Practicas Classroom/8Json/influencers.json'
          ,'r')as archivo2:#abro el archivo y lo guardo en
    #archivo
    Diccionario2=json.load(archivo2)#leo el archivo internamente

if not archivo2.closed:#si el archivo no está cerrrado lo cierro
    print('Cerrando archivo...')
    archivo.close()

print('diccionario: ',Diccionario)
print('Influencer: ',Diccionario2["influencers"][1]["name"])