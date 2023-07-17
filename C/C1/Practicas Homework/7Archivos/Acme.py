'''Este ejercicio lo hemos venido usando para afianzar los conocimientos en listas,
diccionarios y ahora lo usaremos con el tema de archivos de texto en Python. El ejercicio
tendra unos ajustes en los menu s para poder adaptarlo al trabajo con archivos.
La empresa ACME desea que le construya un programa para gestionar la nomina de sus empleados.
Despues de recoger los requerimientos se llego a la decision de gestionar los empleados y
sus nominas a traves del siguiente menu .'''

archivo_empleados = "emplacme.dat"

def verificar():
    # Verificar si el archivo existe
    try:
        with open(archivo_empleados, "r"):
            print("El archivo de empleados existe.")
    except FileNotFoundError:
        print("El archivo de empleados no existe. Se creará uno nuevo.")

        # Crear un nuevo archivo de empleados
        with open(archivo_empleados, "w") as archivo:
            archivo.write("ID;NOMBRE;HORASTRAB;VALHORA\n")

verificar()

'''1. Agregar empleado: Esta opcio n permite adicionar un empleado con su id,
nombre, horas trabajadas y valor de la hora. Los empleados pueden trabajar entre
1 a 160 Horas. Y el valor de la hora puede estar
entre $8,000 y $150,000 pesos la hora.
Cuando se agrega un empleado, se debe agregar tanto en memoria co mo en el archivo.
Para esto puede usar los modos “a” o “w+”. Recuerde el diagrama de flujo de los
modos.'''

# Diccionario para almacenar los empleados y sus datos
empleados = {}

def AgregarEmpleado():
    id_empleado = input("Ingrese el ID del empleado: ")
    if id_empleado in empleados:
        print("El ID del empleado ya existe. Use la opción 'Modificar empleado' para actualizar los datos.")
        return
    
    nombre = input("Ingrese el nombre del empleado: ")
    horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
    valor_hora = float(input("Ingrese el valor de la hora trabajada: "))

    # Validar los límites de horas trabajadas y valor de la hora
    if horas_trabajadas < 1 or horas_trabajadas > 160:
        print("La cantidad de horas trabajadas debe estar entre 1 y 160.")
        return
    if valor_hora < 8000 or valor_hora > 150000:
        print("El valor de la hora trabajada debe estar entre $8,000 y $150,000.")
        return
    # Agregar el empleado al diccionario
    empleados[id_empleado] = {
        'id':id_empleado,
        "nombre": nombre,
        "horas_trabajadas": horas_trabajadas,
        "valor_hora": valor_hora
    }
    with open(archivo_empleados, "a") as archivo:
        escrito = f'{id_empleado};{nombre};{horas_trabajadas};{valor_hora}\n'
        archivo.write(str(escrito)+'\n')
    
    print("Empleado agregado correctamente.")


def mostrarEmpleado():
    with open(archivo_empleados, "r") as archivo:
        contenido = archivo.readlines()

    print("Contenido del archivo:")
    for linea in contenido:
        datos = linea.strip().split(";")
        print(";".join(datos))

'''def ModificarEmpleados():
    id=input('Digite el id del usuario: ')
    with open(archivo_empleados, "a") as archivo:
        for linea in archivo:#recorre cada una de las lineas
            if linea.startswith(id):'''
            
def ModificarEmpleado():
    id_empleado = input('Digite el ID del empleado: ')
    empleados_modificados = []  # Lista para almacenar los empleados modificados
    
    with open(archivo_empleados, "r") as archivo:
        lineas = archivo.readlines()  # Leer todas las líneas del archivo
        
    # Recorrer las líneas y buscar el empleado con el ID correspondiente
    for linea in lineas:
        datos = linea.strip().split(';')  # Separar los datos de la línea por ';'
        if datos[0] == id_empleado:
            nombre = input("Ingrese el nuevo nombre del empleado: ")
            horas_trabajadas = int(input("Ingrese la nueva cantidad de horas trabajadas: "))
            valor_hora = float(input("Ingrese el nuevo valor de la hora trabajada: "))
            
            # Validar los límites de horas trabajadas y valor de la hora
            if horas_trabajadas < 1 or horas_trabajadas > 160:
                print("La cantidad de horas trabajadas debe estar entre 1 y 160.")
                continue
            if valor_hora < 8000 or valor_hora > 150000:
                print("El valor de la hora trabajada debe estar entre $8,000 y $150,000.")
                continue
            
            datos[1] = nombre  # Actualizar el nombre del empleado
            datos[2] = str(horas_trabajadas)  # Actualizar las horas trabajadas
            datos[3] = str(valor_hora)  # Actualizar el valor de la hora
            
            linea_modificada = ';'.join(datos)  # Unir los datos con ';'
            empleados_modificados.append(linea_modificada + '\n')  # Agregar la línea modificada a la lista
        else:
            empleados_modificados.append(linea)  # Conservar las líneas que no corresponden al empleado a modificar
    
    # Guardar los empleados modificados en el archivo
    with open(archivo_empleados, "w") as archivo:
        archivo.writelines(empleados_modificados)
    
    print("Empleado modificado correctamente.")

def BuscarEmpleados():
    pass

def EliminarEmpleados():
    id_empleado = input('Digite el ID del empleado: ')
    
    with open(archivo_empleados, "r") as archivo:
        lineas = archivo.readlines()  # Leer todas las líneas del archivo
        
    # Recorrer las líneas y buscar el empleado con el ID correspondiente
    for linea in lineas:
        if datos[0] == id_empleado:
            datos = linea.pop() 
            print('Usuario eliminado')
        else:
            print('No se encontró el usuario')
    
    # Guardar los empleados modificados en el archivo
    with open(archivo_empleados, "w") as archivo:
        archivo.writelines(linea)
    
    print("Empleado eliminado correctamente.")


def ListarNominaEmpleado():
    pass

def ListarNominaEmpleados():
    pass

def mostrar_menu():
    while True:
        print("*** NOMINA ACME ***")
        print("MENU")
        print("1- Agregar empleado")
        print("2- Modificar empleado")
        print("3- Buscar empleado")
        print("4- Eliminar empleado")
        print("5- Listar empleados")
        print("6- Listar nómina de un empleado")
        print("7- Listar nómina de todos los empleados")
        print("8- Salir")

        opcion = input("Escoja una opción (1-8): ")
        print("--------------------")

        if opcion == "1":
            AgregarEmpleado()
        elif opcion == "2":
            ModificarEmpleado()
        elif opcion == "3":
            BuscarEmpleados()
        elif opcion == "4":
            EliminarEmpleados()
        elif opcion == "5":
            mostrarEmpleado()
        elif opcion == "6":
            ListarNominaEmpleado()
        elif opcion == "7":
            ListarNominaEmpleados()
        elif opcion == "8":
            confirmacion = input("¿Está seguro de que desea salir? (S/N): ")
            if confirmacion.upper() == "S":
                print("¡Hasta luego!")
                break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
        print("--------------------")

# Ejecutar el programa
mostrar_menu()
