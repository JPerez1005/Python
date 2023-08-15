'''Elaborar un programa python que lea varios registros
y descargue esa info en un archivo con formato json que
denomine jugadores.json, la entrada de datos termina
cuando el nombre sea un vacio o un desea continuar'''

import json

# Función para guardar el archivo de datos
def Actualizar(contenido):
    with open('Jugadores.json', 'w') as archivo:
        json.dump(contenido, archivo, indent=4)
    print(f'\nRegistro Agregado...\n')

def registros():
    d=''
    bandera=True
    while bandera==True:
        nombre=input('\nDigite nombre: ')
        if nombre=='':
            print('Saliendo...')
            break
        edad=int(input('Digite edad: '))
        peso=float(input('Digite peso: '))

        data['jugadores'].append({
            'Nombre':nombre,
            'Edad':edad,
            'Peso':peso,
        })

        d=input('Desea continuar?(s/n): ')
        if d=='n' or d=='N':
            bandera=False
            print('Saliendo...')
   

data = {}
data['jugadores']=[]       
registros()
Actualizar(data)