# Importar el módulo
import json
import os
ruta = "Instituto.json"

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


def agregar_estudiante():
    print('Agregar estudiantes: ')
    contenido=AbrirArchivo()
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
    id_estudiante = input('Digite el ID que desea buscar: ')
    contenido = AbrirArchivo()#tambien cargan las variables de los diccionarios
    
    for grupo in contenido.values():
        if id_estudiante in grupo:
            print('-'*30)
            print('Nombre: {:8}'.format(grupo[id_estudiante]['nombre']))
            print('ID    : {:8}'.format(grupo[id_estudiante]['id']))
            print('Sexo  : {:8}'.format(grupo[id_estudiante]['sexo']))
            print('Grupo : {:8}'.format(grupo[id_estudiante]['grupo']))
        else:
            print('Ese estudiante no está registrado...')


def Estudiantes():
    
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
            agregar_estudiante()
        elif elegirop==2:
            ModificarEstudiante()
        elif elegirop==3:
            EliminarEstudiante()
        elif elegirop==4:
            BuscarEstudiante()
        elif elegirop==5:
            print('Saliendo...')
            return

#--------------------------------------------------------------------------------------
#AGREGANDO NOTAS

def AgregarNotas():
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
    id_estudiante = input('Digite el ID del estudiante que desee\nagregar o modificar notas: ')
    contenido = AbrirArchivo()#tambien cargan las variables de los diccionarios
    
    for grupo in contenido.values():
        if id_estudiante in grupo:
            print('\n','-'*30)
            print('Nombre: {:8}'.format(grupo[id_estudiante]['nombre']))
            print('ID    : {:8}'.format(grupo[id_estudiante]['id']))
            estudiantes = contenido[grupo[id_estudiante]['grupo']]
            for estudiante in estudiantes.values():
                estudiante['notas'] = {}#agregamos el campo notas
            Bandera=True
            existencia=True
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
                #          cont anterior,   donde se implantará,   nuevo contenido
                Actualizar(contenido, grupo[id_estudiante]['grupo'], estudiante)
                print("Notas agregadas correctamente.")
                Bandera=False
        else:
            existencia=False

    if existencia==False:
        print('Ese estudiante no está registrado...')

def VerNotas():
    contenido=AbrirArchivo()
    
    for grupo, estudiantes in contenido.items():
        for id_estudiante, estudiante in estudiantes.items():
            if id_estudiante != 'notas':
                if isinstance(estudiante, dict):
                    print('{} {}'.format(estudiante.get('id', ''), estudiante.get('nombre', '')))




def Notas():
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
            AgregarNotas()
        elif elegirop==2:
            AgregarNota()
        elif elegirop==3:
            VerNotas()
        elif elegirop==4:
            print('Saliendo...')
            return

def Reportes(ruta):
    pass



while True:
    op=Menu()
    if op==1:
        Estudiantes()
    elif op==2:
        Notas()
    elif op==3:
        Reportes(ruta)
    elif op==4:
        print('Saliendo...')
        break