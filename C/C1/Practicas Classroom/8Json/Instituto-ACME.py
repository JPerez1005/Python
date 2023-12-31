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
            print('Archivo Creado')
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
            ide=input('Digite el id del estudiante: ')
            if ide.isdigit()==False:
                print('No digite letras en el id...')
                continue
            nombre=input('Digite nombre de estudiante: ')
            if nombre.isalpha()==False:
                print('No digite numeros en el nombre...')
                continue
            sex=input('Digite el sexo del estudiante(m/f): ')
            if sex.lower()!='m':
                if  sex.lower()!='f':
                    print('tiene que digitar (m) o (f)...')
                    continue
            classroom=input('Digite el grado del estudiante: ')
            with open(ruta, "r") as archivo:
                contenido = json.load(archivo)
            grado ={
                'id':ide,
                'nombre':nombre,
                'sexo':sex,
                'grado':classroom
            }
            contenido[classroom]=grado
            with open(ruta,'w') as archivo:
                json.dump(contenido, archivo)
            
            print('Estudiante registrado correctamente...')
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