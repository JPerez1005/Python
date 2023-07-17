# Importar el módulo
#REcuerde al final subir el archivo al git hub(classroom)
#y comentar el git hub en classroom
import json
import os
ruta = "Archivo.json"#Aquí coloque el archivo que usará

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

while True:
    clear()
    contenido=AbrirArchivo()#para cargar datos usar el contenido en cada funcion
    op=Menu()
    if op==1:
        clear()
        #Aqui´coloque las funciones
    elif op==2:
        clear()
        #Aqui´coloque las funciones
    elif op==3:
        clear()
        #Aqui´coloque las funciones
    elif op==4:
        clear()
        print('Saliendo...')
        break