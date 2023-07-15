import json
import os

ruta = "colegio.json"

def crear_archivo_json():
    if not os.path.exists(ruta):
        with open(ruta, 'w') as archivo:
            json.dump({}, archivo)
        print("Archivo JSON creado exitosamente.")
    else:
        print("El archivo ya existe. No se creó uno nuevo.")

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


def agregar_estudiante():
    grupo = input("Ingrese el grupo del estudiante: ")
    id_estudiante = input("Ingrese el ID del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = input("Ingrese la edad del estudiante: ")

    # Abrir el archivo JSON en modo lectura
    contenido=AbrirArchivo()

    # Verificar si el grupo ya existe en el colegio
    usuarios=Agrupaciones(grupo,contenido)

    # Agregar el estudiante al grupo
    usuarios[id_estudiante] = {
        'id':id_estudiante,
        "nombre": nombre,
        "edad": edad
    }

    # Sobrescribir el archivo JSON con los datos actualizados
    Actualizar(contenido,grupo,usuarios)

    print("Estudiante agregado correctamente.")

# Crear el archivo JSON si no existe
crear_archivo_json()

# Agregar estudiantes al colegio
while True:
    agregar_estudiante()
    respuesta = input("¿Desea agregar más estudiantes? (s/n): ")
    if respuesta.lower() != "s":
        break
