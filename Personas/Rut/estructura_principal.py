import json
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def CargarDatos(NombreArchivo):
    try:
        with open(NombreArchivo, 'r') as archivo:
            contenido = json.load(archivo)
    except FileNotFoundError:#si no encuentra el archivo lo creamos
        contenido = {}
        contenido['animales']={}
        contenido['animales']['dela_selva']=[]
        contenido['animales']['del_mar']=[]
        contenido['animales']['del_cielo']=[]
    return contenido

# Función para guardar el archivo de datos
def Actualizar(NombreArchivo, contenido):
    with open(NombreArchivo, 'w') as archivo:
        json.dump(contenido, archivo, indent=4, ensure_ascii=False)

#para que el usuario no digite numeros
def validacion_letras(variable):
    while True:
        if variable.isdigit():
            print(f'No digite numeros...')
            variable=input(f'vuelva a digitar: ')
            continue
        else:
            return

#para que el usuario no digite letras
def validacion_numeros(variable):
    while True:
        try:
            variable=int(variable)
            return variable
        except ValueError:
            print(f'No digite letras...')
            variable=input(f'vuelva a digitar: ')

def agregar(contenido):
    clear()
    nombre=input('Nombre del animal: ')
    validacion_letras(nombre)
    
    #lo siguiente es para agregar valores predefinidos
    print()
    
    while True:
        print('1.Grande | 2.Mediano | 3.Pequeño')
        tamaño=input('Digite el tamaño del animal: ')
        tamaño=validacion_numeros(tamaño)
        if tamaño==1:
            tamaño='grande'
            break
        elif tamaño==2:
            tamaño='mediano'
            break
        elif tamaño==3:
            tamaño='pequeño'
            break
        else:
            print('Opción no valida...')
    
    #lo siguiente es para agregar muchos valores
    habilidades=[]
    while True:
        print('Para salir presione (enter)')
        habilidad=input(f'Digite una habilidad del {nombre}: ')
        validacion_letras(habilidad)
        if habilidad:
            habilidades.append(habilidad)
        else:
            break
    contenido['animales']['dela_selva'].append({
        'nombre':nombre,
        'tamaño':tamaño,
        'habilidades':habilidades
    })
    
    print('Datos Agregados Correctamente')
    input('Presione cualquier tecla para continuar...')

def busqueda(contenido):
    clear()
    nombre=input('Digite un nombre a buscar: ')
    cantidad_animales=len(contenido['animales']['dela_selva'])#cantidad de animales de la selva
    animal=contenido['animales']['dela_selva']
    print(cantidad_animales)
    for i in range(0,cantidad_animales-1):
        if nombre==animal[i]['nombre']:
            print('El nombre existe')
            print(f'nombre: {animal[i]["nombre"]}')
            print(f'tamaño: {animal[i]["tamaño"]}')
            print(f'habilidades: {animal[i]["habilidades"]}')
            input('Digite cualquier tecla para continuar...')
            return
    print('no se encontró el nombre')
    input('Digite cualquier tecla para continuar')

def listado(contenido):
    clear()
    print('Listado de animales de la SELVA...')
    cantidad_animales=len(contenido['animales']['dela_selva'])#cantidad de animales de la selva
    animal=contenido['animales']['dela_selva']
    for i in range(0,cantidad_animales):
            print('-'*40)
            print()
            print(f'nombre: {animal[i]["nombre"]}')
            print(f'tamaño: {animal[i]["tamaño"]}')
            print(f'habilidades: {animal[i]["habilidades"]}')
            input('Digite cualquier tecla para continuar...')

def modificar(contenido):
    clear()
    nombre=input('Digite un nombre a buscar: ')
    cantidad_animales=len(contenido['animales']['dela_selva'])#cantidad de animales de la selva
    animal=contenido['animales']['dela_selva']
    for i in range(0,cantidad_animales):
        if nombre==animal[i]['nombre']:
            print('El nombre existe')
            print(f'nombre: {animal[i]["nombre"]}')
            print(f'tamaño: {animal[i]["tamaño"]}')
            print(f'habilidades: {animal[i]["habilidades"]}')
            input('Digite cualquier tecla para continuar...')
            nombre=input('Nombre del animal: ')
            validacion_letras(nombre)
            
            #lo siguiente es para agregar valores predefinidos
            print()
            
            while True:
                print('1.Grande | 2.Mediano | 3.Pequeño')
                tamaño=input('Digite el tamaño del animal: ')
                tamaño=validacion_numeros(tamaño)
                if tamaño==1:
                    tamaño='grande'
                    break
                elif tamaño==2:
                    tamaño='mediano'
                    break
                elif tamaño==3:
                    tamaño='pequeño'
                    break
                else:
                    print('Opción no valida...')
            
            #lo siguiente es para agregar muchos valores
            habilidades=[]
            while True:
                print('Para salir presione (enter)')
                habilidad=input(f'Digite una habilidad del {nombre}: ')
                validacion_letras(habilidad)
                if habilidad:
                    habilidades.append(habilidad)
                else:
                    break
            contenido['animales']['dela_selva'][i]=({
                'nombre':nombre,
                'tamaño':tamaño,
                'habilidades':habilidades
            })
            return
    print('no se encontró el animal')
    input('Digite cualquier tecla para continuar')

def eliminar(contenido):
    clear()
    nombre=input('Digite un nombre a buscar: ')
    cantidad_animales=len(contenido['animales']['dela_selva'])#cantidad de animales de la selva
    animal=contenido['animales']['dela_selva']
    for i in range(0,cantidad_animales):
        if nombre==animal[i]['nombre']:
            print('El animal existe')
            print(f'nombre: {animal[i]["nombre"]}')
            print(f'tamaño: {animal[i]["tamaño"]}')
            print(f'habilidades: {animal[i]["habilidades"]}')
            d=input('Digite (s) para eliminar, para cancelar digite una letra diferente: ')
            if d.lower()=='s':
                del contenido['animales']['dela_selva'][i]#eliminamos todo el contenido de esa posición
                print('Registro Eliminado correctamente...')
            else:
                print('Cancelada la eliminacion de registro...')
                input('Digite cualquier letra para continuar...')
    print('No se encontró el animal...')
    input('Digite cualquier letra para continuar...')

def menu():
    clear()
    Archivo='Animales.json'#nombre del archivo...
    contenido = CargarDatos(Archivo)#ahora todo el contenido del archivo esta guardado en la variable contenido
    #en contenido se muestran los datos de ese archivo
    while True:
        print()
        print('---TITULO---')
        print()
        print('1. agregar')
        print('2. buscar')
        print('3. enlistar')
        print('4. modificar')
        print('5. eliminar')
        print('6. Salir')
        
        opcion = input('Seleccione una opción: ')
        if opcion.isalpha():
            print('No digite letras')
            clear()
            continue#continue lo que hace es volver a iniciar el ciclo while
        if opcion == '1':
            agregar(contenido)
            Actualizar(Archivo,contenido)#actualizamos la informacion del contenido
            clear()
        elif opcion == '2':
            busqueda(contenido)
            Actualizar(Archivo,contenido)#actualizamos la informacion del contenido
            clear()
        elif opcion == '3':
            listado(contenido)
            Actualizar(Archivo,contenido)#actualizamos la informacion del contenido
            clear()
        elif opcion == '4':
            modificar(contenido)
            Actualizar(Archivo,contenido)#actualizamos la informacion del contenido
            clear()
        elif opcion == '5':
            eliminar(contenido)
            Actualizar(Archivo,contenido)#actualizamos la informacion del contenido
            clear()
        elif opcion == '6':
            # Guardar los productos y clientes en los archivos antes de salir
            print('SALIENDO...')
            break
        else:
            print('Opción inválida. Por favor, seleccione nuevamente.')
    
    print('¡Hasta luego!')

menu()