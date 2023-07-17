import json

# Función para abrir el archivo de datos
def CargarDatos(NombreArchivo):
    try:
        with open(NombreArchivo, 'r') as archivo:
            contenido = json.load(archivo)
    except FileNotFoundError:
        contenido = []
    return contenido

# Función para guardar el archivo de datos
def Actualizar(NombreArchivo, contenido):
    with open(NombreArchivo, 'w') as archivo:
        json.dump(contenido, archivo)

Archivo = 'archivo.json'  # Nombre del archivo para almacenar los datos

# Abrir el archivo y cargar los datos existentes
contenido = CargarDatos(Archivo)

# Menú principal del programa
def menu():
    while True:
        print('--- Registro e Informe de Notas ---')
        print('1. Ingresar Estudiante')
        print('2. Modificar Estudiante')
        print('3. Buscar Estudiante')
        print('4. Eliminar Estudiante')
        print('5. Registrar Notas')
        print('6. Listado de Notas Promedios por Grado')
        print('7. Terna de Excelencia por Grado')
        print('8. Terna de Excelencia del Colegio')
        print('9. Salir')

        opcion = input('Seleccione una opción: ')
        if opcion == '1':
            IngresarEstudiante()
        elif opcion == '2':
            ModificarEstudiante()
        elif opcion == '3':
            BuscarEstudiante()
        elif opcion == '4':
            EliminarEstudiante()
        elif opcion == '5':
            RegistrarNotas()
        elif opcion == '6':
            ListadoNotasPromedios()
        elif opcion == '7':
            TernaExcelenciaGrado()
        elif opcion == '8':
            TernaExcelenciaColegio()
        elif opcion == '9':
            # Guardar los datos en el archivo antes de salir
            Actualizar(Archivo, contenido)
            break
        else:
            print('Opción inválida. Por favor, seleccione nuevamente.')

    print('¡Hasta luego!')

def IngresarEstudiante():
    print('--- Ingresar Estudiante ---')
    id_estudiante = input('ID del estudiante: ')
    nombre = input('Nombre del estudiante: ')
    sexo = input('Sexo del estudiante: ')
    grado = input('Grado del estudiante: ')

    estudiante = {
        'id': id_estudiante,
        'nombre': nombre,
        'sexo': sexo,
        'grado': grado,
        'notas': []
    }

    contenido.append(estudiante)
    print('Estudiante agregado correctamente.')

def ModificarEstudiante():
    print('--- Modificar Estudiante ---')
    id_estudiante = input('ID del estudiante a modificar: ')

    estudiante = next((e for e in contenido if e['id'] == id_estudiante), None)
    if estudiante is None:
        print('Estudiante no encontrado.')
        return

    print('Estudiante encontrado. Datos actuales:')
    print('ID:', estudiante['id'])
    print('Nombre:', estudiante['nombre'])
    print('Sexo:', estudiante['sexo'])
    print('Grado:', estudiante['grado'])

    nuevo_nombre = input('Nuevo nombre (dejar en blanco para mantener el actual): ')
    nuevo_sexo = input('Nuevo sexo (dejar en blanco para mantener el actual): ')
    nuevo_grado = input('Nuevo grado (dejar en blanco para mantener el actual): ')

    if nuevo_nombre:
        estudiante['nombre'] = nuevo_nombre
    if nuevo_sexo:
        estudiante['sexo'] = nuevo_sexo
    if nuevo_grado:
        estudiante['grado'] = nuevo_grado

    print('Estudiante modificado correctamente.')

def BuscarEstudiante():
    print('--- Buscar Estudiante ---')
    id_estudiante = input('ID del estudiante a buscar: ')

    estudiante = next((e for e in contenido if e['id'] == id_estudiante), None)
    if estudiante is None:
        print('Estudiante no encontrado.')
        return

    print('Estudiante encontrado. Información:')
    print('ID:', estudiante['id'])
    print('Nombre:', estudiante['nombre'])
    print('Sexo:', estudiante['sexo'])
    print('Grado:', estudiante['grado'])

def EliminarEstudiante():
    print('--- Eliminar Estudiante ---')
    id_estudiante = input('ID del estudiante a eliminar: ')

    estudiante = next((e for e in contenido if e['id'] == id_estudiante), None)
    if estudiante is None:
        print('Estudiante no encontrado.')
        return

    contenido.remove(estudiante)
    print('Estudiante eliminado correctamente.')

def RegistrarNotas():
    print('--- Registrar Notas ---')
    grupo = input('Ingrese el grupo al cual desea ingresar notas: ')

    estudiantes_grupo = [e for e in contenido if e['grado'] == grupo]
    if len(estudiantes_grupo) == 0:
        print('No existen estudiantes en el grupo especificado.')
        return

    print(f'Lista de estudiantes del grupo {grupo}:')
    for estudiante in estudiantes_grupo:
        print('ID:', estudiante['id'])
        print('Nombre:', estudiante['nombre'])
        print('Sexo:', estudiante['sexo'])
        print('Grado:', estudiante['grado'])
        print()

        while True:
            nota = input('Ingrese una nota (o "fin" para terminar): ')
            if nota.lower().strip() == 'fin':
                break
            estudiante['notas'].append(float(nota))

    print('Notas registradas correctamente.')

def ListadoNotasPromedios():
    print('--- Listado de Notas Promedios por Grado ---')

    promedios_por_grado = {}

    for estudiante in contenido:
        grado = estudiante['grado']
        notas = estudiante['notas']

        if len(notas) > 0:
            promedio = sum(notas) / len(notas)
        else:
            promedio = 0

        if grado in promedios_por_grado:
            promedios_por_grado[grado].append({
                'id': estudiante['id'],
                'nombre': estudiante['nombre'],
                'promedio': promedio
            })
        else:
            promedios_por_grado[grado] = [{
                'id': estudiante['id'],
                'nombre': estudiante['nombre'],
                'promedio': promedio
            }]

    for grado, estudiantes in promedios_por_grado.items():
        print(f'Grado: {grado}')
        for estudiante in estudiantes:
            print('ID:', estudiante['id'])
            print('Nombre:', estudiante['nombre'])
            print('Promedio:', estudiante['promedio'])
            print()

def TernaExcelenciaGrado():
    print('--- Terna de Excelencia por Grado ---')

    grado = input('Ingrese el grado para mostrar la terna de excelencia: ')

    estudiantes_grado = [e for e in contenido if e['grado'] == grado]
    if len(estudiantes_grado) == 0:
        print('No existen estudiantes en el grado especificado.')
        return

    estudiantes_grado.sort(key=lambda e: sum(e['notas']) / len(e['notas']), reverse=True)

    print(f'Terna de excelencia del grado {grado}:')
    for i, estudiante in enumerate(estudiantes_grado[:5]):
        print(f'Puesto {i+1}:')
        print('Nombre:', estudiante['nombre'])
        print('Promedio:', sum(estudiante['notas']) / len(estudiante['notas']))
        print()

def TernaExcelenciaColegio():
    print('--- Terna de Excelencia del Colegio ---')

    estudiantes_colegio = []

    for estudiante in contenido:
        if len(estudiante['notas']) > 0:
            promedio = sum(estudiante['notas']) / len(estudiante['notas'])
        else:
            promedio = 0

        estudiantes_colegio.append({
            'nombre': estudiante['nombre'],
            'grado': estudiante['grado'],
            'promedio': promedio
        })

    estudiantes_colegio.sort(key=lambda e: e['promedio'], reverse=True)

    print('Terna de excelencia del colegio:')
    for i, estudiante in enumerate(estudiantes_colegio[:5]):
        print(f'Puesto {i+1}')
        print('Nombre:', estudiante['nombre'])
        print('Grado:', estudiante['grado'])
        print('Promedio:', estudiante['promedio'])
        print()

# Menú principal del programa
menu()
