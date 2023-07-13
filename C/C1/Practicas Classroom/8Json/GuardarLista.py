import json

lista=[10,20,30,40,60]

with open('C/C1/Practicas Classroom/8Json/lista.json','w') as archivo:
    json.dump(lista, archivo)
    print('Se ah escrito en disco...')
    
if not archivo.closed:
    print('Cerrando archivo...')
    archivo.close()
    
print('Seah cerrado el archivo...')