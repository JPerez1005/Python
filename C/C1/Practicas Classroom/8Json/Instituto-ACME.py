import json

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
            print("Error! Ingrese un numero valido")


def msgError(msg):
    print("----> ¡ERROR!" + msg)
    input("---> Presione ENTER para continuar")

def CargarInfo(ruta,dic):
    with open(ruta,'a+') as archivo:
        archivo.seek(0)
        
        try:
            json.load(archivo,dic)
        except Exception as e:
            dic = {}
    
    print(dic)

ruta='instituto.json'
dicdata={}
CargarInfo(ruta,dicdata)
def Menu():
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

def Estudiantes(ruta):
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
    
    while True:
        if elegirop==1:
            print('Agregar estudiantes: ')
        elif elegirop==2:
            print('Modificar Estudiantes')
        elif elegirop==3:
            print('Eliminar Estudiantes')
        elif elegirop==4:
            print('Buscar Estudiantes')
        elif elegirop==5:
            print('Saliendo...')
            return

def Notas(ruta):
    pass

def Reportes(ruta):
    pass



while True:
    op=Menu()
    if op==1:
        Estudiantes(ruta)
    elif op==2:
        Notas(ruta)
    elif op==3:
        Reportes(ruta)
    elif op==4:
        print('Saliendo...')
        break