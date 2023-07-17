# Importar el módulo
import json
import os
ruta = "Instituto.json"

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                print("Error! El codigo debe ser entero postivo.")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError:
            print("Error! Ingrese un numero valido: ")

def msgError(msg):
    print("----> ¡ERROR!" + msg)
    input("---> Presione ENTER para continuar")

def crear_archivo_json():
    if not os.path.exists(ruta):# si el archivo ya existe entonces...
        colegio = {}  # Creamos el diccionario de colegio
        with open(ruta, 'w') as archivo:
            json.dump(colegio, archivo)
        print("Archivo JSON creado exitosamente.")
    else:
        print("El archivo ya existe. No se creó uno nuevo.")

def verificar_archivo_vacio():
    with open(ruta, 'r') as archivo:
        contenido = json.load(archivo)
        
        if contenido: # Verificar si el contenido del archivo no está vacío
            print("El archivo contiene datos.")
        else:
            print("El archivo está vacío.")

def Menu():
    clear()
    crear_archivo_json()
    verificar_archivo_vacio()
    print("\n---------------")
    print(" ESTUDIANTES ACME MENU: ")
    print("----------------\n")
    print("1.Gestión Estudiantes")
    print("2.Gestión Notas")
    print("3.Gestión Reportes")
    print("4.Salir")
    print(">> Escoja una opcion (1-4)?")
    elegirop = leerInt("\n>> Opcion (1 a 4)?: ")
    if elegirop < 1 or elegirop > 4:
        msgError("Ingrese una opcion valida")
    return elegirop

def AbrirArchivo():
    with open(ruta, "r") as archivo:
        contenido = json.load(archivo)
        return contenido

def Actualizar(contenido,identificador,entrada):
    # Actualizar el grupo en el colegio
    contenido[identificador] = entrada
    with open(ruta, "w") as archivo:
        json.dump(contenido, archivo)

def Agrupaciones(var,contenido):
    if var in contenido:
        usuarios = contenido[var]
    else:
        usuarios = {}
    
    return usuarios

'''def UsuarioExistente(id,classroom,existe):
    # Abrir el archivo JSON en modo lectura
    contenido=AbrirArchivo()
    
    # Verificar si el grupo ya existe en el colegio
    usuarios=Agrupaciones(classroom,contenido)
    if classroom in contenido.keys():
        if id in usuarios.keys():
            print('ese id ya existe')
            existe=True
    return existe'''

def UsuarioExistente(id, contenido):
    for grupo in contenido.values():
        if id in grupo:
            print('Ese ID ya existe en algún grupo')
            return True
    return False

#--------------------------------------------------------------------------------------
#AGREGANDO ESTUDIANTES

def agregar_estudiante():
    clear()
    print('Agregar estudiantes: ')
    contenido=AbrirArchivo()#cargar datos existentes
    NumRegistros=leerInt('Cuantos estudiantes desea agregar?: ')
    for i in range(1,NumRegistros+1):
        # Abrir el archivo JSON en modo lectura
        classroom=input('Digite el grado del estudiante: ')
        ide=input('Digite el id del estudiante: ')
        if ide.isdigit()==False:
            print('No digite letras en el id...')
            return
        existe=False
        existe=UsuarioExistente(ide,contenido)
        if existe==True:
            print('Ese estudiante ya existe')
            return
        nombre=input('Digite nombre de estudiante: ')
        if nombre.isalpha()==False:
            print('No digite numeros en el nombre...')
            return
        sex=input('Digite el sexo del estudiante(m/f): ')
        if sex.lower()!='m':
            if  sex.lower()!='f':
                print('tiene que digitar (m) o (f)...')
                return

        # Verificar si el grupo ya existe en el colegio
        usuarios=Agrupaciones(classroom,contenido)

        # Agregar el estudiante al grupo
        usuarios[ide] = {
            'id':ide,
            "nombre": nombre,
            "sexo": sex,
            'grupo':classroom
        }

        # Sobrescribir el archivo JSON con los datos actualizados
        Actualizar(contenido,classroom,usuarios)

        print("Estudiante agregado correctamente.")
    return

def ModificarEstudiante():
    clear()
    id_estudiante = input('Digite el ID que desea modificar: ')
    contenido = AbrirArchivo()#tambien cargan las variables de los diccionarios
    
    existe = UsuarioExistente(id_estudiante,contenido)
    
    if existe:
        print("El estudiante con el ID", id_estudiante, "existe.")
        
        classroom=input('Digite el nuevo grado del estudiante: ')
        nombre=input('Digite el nuevo nombre de estudiante: ')
        if nombre.isalpha()==False:
            print('No digite numeros en el nombre...')
            return
        sex=input('Digite el nuevo sexo del estudiante(m/f): ')
        if sex.lower()!='m':
            if  sex.lower()!='f':
                print('tiene que digitar (m) o (f)...')
                return
        # Verificar si el grupo ya existe en el colegio
        usuarios=Agrupaciones(classroom,contenido)
        
        # Agregar el estudiante al grupo
        usuarios[id_estudiante] = {
            'id':id_estudiante,
            "nombre": nombre,
            "sexo": sex,
            'grupo':classroom
        }
        # Sobrescribir el archivo JSON con los datos actualizados
        Actualizar(contenido,classroom,usuarios)

        print("Estudiante Modificado correctamente.")
        return
    else:
        print("El estudiante con el ID", id_estudiante, "no existe.")
        return

def EliminarEstudiante():
    clear()
    id_estudiante = input('Digite el ID que desea eliminar: ')
    contenido = AbrirArchivo()#tambien cargan las variables de los diccionarios
    bandera=True
    for grupo in contenido.values():
        if id_estudiante in grupo:
            print('El estudiante existe.')
            del grupo[id_estudiante]
            Actualizar(contenido, id_estudiante,grupo )
            print("Estudiante eliminado correctamente.")
            bandera=True
            break
        else:
            bandera=False
    if bandera==False:
        print('No se encontró el usuario...')

def BuscarEstudiante():
    clear()
    id_estudiante = input('Digite el ID que desea buscar: ')
    contenido = AbrirArchivo()#tambien cargan las variables de los diccionarios
    existe=True
    for grupo in contenido.values():
        if id_estudiante in grupo:
            print('-'*30)
            print('Nombre: {:8}'.format(grupo[id_estudiante]['nombre']))
            print('ID    : {:8}'.format(grupo[id_estudiante]['id']))
            print('Sexo  : {:8}'.format(grupo[id_estudiante]['sexo']))
            print('Grupo : {:8}'.format(grupo[id_estudiante]['grupo']))
            existe=True
            break
        else:
            existe=False
    if existe==False:
        print('Ese estudiante no está registrado...')


def Estudiantes():
    clear()
    while True:
        print('\n','-'*20)
        print('GESTION DE ESTUDIANTES')
        print('-'*20,'\n')
        print("1. Agregar Estudiantes")
        print("2. Modificar Estudiantes")
        print("3. Eliminar Estudiantes")
        print("4. Buscar Estudiantes")
        print('5. Salir')
        print(">> Escoja una opcion (1-5)?")
        elegirop = leerInt("\n>> Opcion (1 a 5)?: ")
        if elegirop < 1 or elegirop > 5:
            msgError("Ingrese una opcion valida")
        if elegirop==1:
            clear()
            agregar_estudiante()
        elif elegirop==2:
            clear()
            ModificarEstudiante()
        elif elegirop==3:
            clear()
            EliminarEstudiante()
        elif elegirop==4:
            clear()
            BuscarEstudiante()
        elif elegirop==5:
            print('Saliendo...')
            return

#--------------------------------------------------------------------------------------
#AGREGANDO NOTAS

def AgregarNotas():
    clear()
    g=input('Digite el grupo donde quiere ingresar las notas: ')
    contenido=AbrirArchivo()
    if g in contenido:
        print('El grupo si está registrado')
        # Obtener el diccionario de estudiantes del grupo
        estudiantes = contenido[g]
        nombres=sorted([estudiante['nombre'] for estudiante in estudiantes.values()])
        
        # Agregar el campo de notas a cada estudiante
        for estudiante in estudiantes.values():
            estudiante['notas'] = {}
        
        for nombre in nombres:#de forma alfabetica por nombres    
            for estudiante in estudiantes.values():
                if estudiante['nombre'] == nombre:#para que no se repitan los nombres
                    id_estudiante = estudiante['id']
                    print('{:2} {:4}'.format(id_estudiante, nombre))
                    Bandera=True
                    while Bandera==True:
                        try:
                            nota1=float(input('Digite la nota 1: '))
                            nota2=float(input('Digite la nota 2: '))
                            nota3=float(input('Digite la nota 3: '))
                            if nota1 < 1 or nota1 > 5 or nota2 < 1 or nota2 > 5 or nota3 < 1 or nota3 > 5:
                                raise Exception()
                            prom=(nota1+nota2+nota3)//3
                        except ValueError:
                            print('No digite letras...')
                            continue
                        except Exception as error:
                            print('Las notas deben estar en el rango de 1 a 5')
                            continue
                        # Guardar las notas en el diccionario de notas del estudiante
                        estudiante['notas'] = {
                            'nota1': nota1,
                            'nota2': nota2,
                            'nota3': nota3,
                            'promedio': prom
                        }
                        #contenido=contenido anterior
                        #g=Donde se guardará
                        #estudiantes=todos los nuevos estudiantes
                        Actualizar(contenido, g, estudiantes)
                        print("Notas agregadas correctamente.")
                        Bandera=False
                    break
    else:
        print('Ese grupo no existe')

def AgregarNota():
    clear()
    contenido = AbrirArchivo()
    id_estudiante = input('Digite el ID del estudiante: ')
    encontrado = False

    #se busca por medio de items, el grupo y en estudiante estan los ids
    for grupo, estudiantes in contenido.items():
        #si el id anteriormente registrado está en los ids
        if id_estudiante in estudiantes:
            #odtenemos los datos del estudiante
            estudiante = estudiantes[id_estudiante]
            
            nombre_estudiante = estudiante['nombre']#nombre del estudiante
            grupo_estudiante = estudiante['grupo']#grupo del estudiante
            print('El estudiante con ID {} está registrado en el grupo {}'.format(id_estudiante, grupo_estudiante))
            print('{:4} {:2}'.format(id_estudiante, nombre_estudiante))
            Bandera = True
            while Bandera:
                try:
                    nota1 = float(input('Digite la nota 1: '))
                    nota2 = float(input('Digite la nota 2: '))
                    nota3 = float(input('Digite la nota 3: '))
                    if nota1 < 1 or nota1 > 5 or nota2 < 1 or nota2 > 5 or nota3 < 1 or nota3 > 5:
                        raise Exception()
                    prom = (nota1 + nota2 + nota3) / 3
                except ValueError:
                    print('No digite letras...')
                    continue
                except Exception as error:
                    print('Las notas deben estar en el rango de 1 a 5')
                    continue
                # Guardar las notas en el diccionario de notas del estudiante
                estudiante['notas'] = {
                    'nota1': nota1,
                    'nota2': nota2,
                    'nota3': nota3,
                    'promedio': prom
                }
                Actualizar(contenido, grupo, estudiantes)
                print("Notas agregadas correctamente.")
                Bandera = False
            encontrado = True
            break

    if not encontrado:
        print('No se encontró ningún estudiante con el ID especificado.')

def VerNotas():
    clear()
    contenido = AbrirArchivo()#cargamos todo el contenido
    for grupo, estudiantes in contenido.items():
        print('GRUPO: {}'.format(grupo))
        for id_estudiante, estudiante in estudiantes.items():
            if isinstance(estudiante, dict):#evitar errores por si algun
                #valor de estudiante es un diccionario
                print('{:10} {:2}'.format(estudiante.get('id', ''), estudiante.get('nombre', '')))
                notas = estudiante.get('notas', {})
                notasE='notas' in estudiante
                for clave in sorted(notas.keys()):
                    valor = notas[clave]
                    print('{:10}: {:2}'.format(clave, valor))
                if notasE==False:
                    print('El estudiante no tiene notas')
                print()

def Notas():
    clear()
    while True:
        print('\n','-'*20)
        print('GESTION DE NOTAS')
        print('-'*20,'\n')
        print("1. Agregar Notas de Estudiantes")
        print("2. Agregar Notas de algún Estudiantes")
        print("3. Ver Notas")
        print("4. Salir")
        print(">> Escoja una opcion (1-5)?")
        elegirop = leerInt("\n>> Opcion (1 a 5)?: ")
        if elegirop < 1 or elegirop > 5:
            msgError("Ingrese una opcion valida")
        if elegirop==1:
            clear()
            AgregarNotas()
        elif elegirop==2:
            clear()
            AgregarNota()
        elif elegirop==3:
            clear()
            VerNotas()
        elif elegirop==4:
            print('Saliendo...')
            return

#--------------------------------------------------------------------------------------
#AGREGANDO REPORTES

def ExcelenciaGrado():
    clear()
    lista=[]
    contenido = AbrirArchivo()#cargamos todo el contenido
    g=input('Digite el grupo para ver las mejores notas: ')
    existencia=False
    for grupo,Estudiantes in contenido.items():
        if g==grupo:
            existencia=True
            for idEstudiante,estudiante in Estudiantes.items():
                if isinstance(estudiante, dict):#evitar errores por si algun
                #valor de estudiante es un diccionario
                    notas = estudiante.get('notas', {})
                    promedio = notas.get('promedio')
                    if promedio is not None:#si el promedio no esta vacio
                        lista.append({'nombre': estudiante['nombre'], 'promedio': promedio})
                    else:
                        print("No se encontró el promedio de notas.")
    if existencia==False:
        print('El grupo no existe...')
    # Ordenar la lista en función del promedio de mayor a menor
    lista_ordenada = sorted(lista, key=lambda x: x['promedio'], reverse=True)

    # Mostrar los cinco estudiantes con mejor promedio
    print('Los cinco estudiantes con mejor promedio:')
    for i, estudiante in enumerate(lista_ordenada[:5]):
        print(f'{i+1}. {estudiante["nombre"]}: {estudiante["promedio"]}')

def ExcelenciaColegio():
    clear()
    lista=[]
    contenido = AbrirArchivo()#cargamos todo el contenido
    existencia=False
    for grupo,Estudiantes in contenido.items():
        existencia=True
        for idEstudiante,estudiante in Estudiantes.items():
            if isinstance(estudiante, dict):#evitar errores por si algun
            #valor de estudiante es un diccionario
                notas = estudiante.get('notas', {})
                promedio = notas.get('promedio')
                if promedio is not None:#si el promedio no esta vacio
                    lista.append({'nombre': estudiante['nombre'], 'promedio': promedio, 'grupo':estudiante['grupo']})
                else:
                    print("No se encontró el promedio de notas.")
    # Ordenar la lista en función del promedio de mayor a menor
    lista_ordenada = sorted(lista, key=lambda x: x['promedio'], reverse=True)

    # Mostrar los cinco estudiantes con mejor promedio
    print('Los cinco estudiantes con mejor promedio del colegio son:')
    for i, estudiante in enumerate(lista_ordenada[:5]):#recorremos los primeros cinco elementos
        print(f'{i+1}. {estudiante["nombre"]}: {estudiante["promedio"]}: {estudiante["grupo"]}')

def Reportes(ruta):
    clear()
    while True:
        print('\n','-'*20)
        print('GESTION DE NOTAS')
        print('-'*20,'\n')
        print("1. Excelencia por grado")
        print("2. Excelencia del colegio")
        print("3. Salir")
        print(">> Escoja una opcion (1-3)?")
        elegirop = leerInt("\n>> Opcion (1 a 3)?: ")
        if elegirop < 1 or elegirop > 3:
            msgError("Ingrese una opcion valida")
        if elegirop==1:
            clear()
            ExcelenciaGrado()
        elif elegirop==2:
            clear()
            ExcelenciaColegio()
        elif elegirop==3:
            print('Saliendo...')
            return



while True:
    clear()
    op=Menu()
    if op==1:
        clear()
        Estudiantes()
    elif op==2:
        clear()
        Notas()
    elif op==3:
        clear()
        Reportes(ruta)
    elif op==4:
        clear()
        print('Saliendo...')
        break