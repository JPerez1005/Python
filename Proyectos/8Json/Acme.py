import json
import os

archivo_empleados = "emplacme.json"

def crear_archivo_json():
    if not os.path.exists(archivo_empleados):# si el archivo ya existe entonces...
        empleados = {}  # Creamos el diccionario de empleados
        with open(archivo_empleados, 'w') as archivo:
            json.dump(empleados, archivo)
        print("Archivo JSON creado exitosamente.")
    else:
        print("El archivo ya existe. No se creó uno nuevo.")


def verificar_archivo_vacio():
    with open(archivo_empleados, 'r') as archivo:
        contenido = json.load(archivo)
        
        if contenido: # Verificar si el contenido del archivo no está vacío
            print("El archivo contiene datos.")
        else:
            print("El archivo está vacío.")

def AgregarEmpleado():

    # Solicitar los datos del nuevo empleado
    id_empleado = input("Ingrese el ID del empleado: ")
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

    # Abrir el archivo JSON en modo lectura
    with open(archivo_empleados, "r") as archivo:
        contenido = json.load(archivo)  # Cargar el contenido actual del archivo

    # Agregar el nuevo empleado al diccionario de empleados
    empleado = {
        'id': id_empleado,
        'nombre': nombre,
        'horas trabajadas': horas_trabajadas,
        'valor hora': valor_hora
    }
    contenido[id_empleado] = empleado

    # Sobrescribir el archivo JSON con los datos actualizados
    with open(archivo_empleados, "w") as archivo:
        json.dump(contenido, archivo)

    print("Empleado agregado correctamente.")

def ModificarEmpleado():
    verificar_archivo_vacio()
    IdMod=input('Digite el id a modificar: ')
    # Abrir el archivo JSON en modo lectura
    with open(archivo_empleados, "r") as archivo:
        contenido = json.load(archivo)  # Cargar el contenido actual del archivo
    
    if IdMod in contenido:
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
    
        # Agregar el nuevo empleado al diccionario de empleados
        empleado = {
            'id': IdMod,
            'nombre': nombre,
            'horas trabajadas': horas_trabajadas,
            'valor hora': valor_hora
        }
        contenido[IdMod] = empleado

        # Sobrescribir el archivo JSON con los datos actualizados
        with open(archivo_empleados, "w") as archivo:
            json.dump(contenido, archivo)

        print("Empleado modificado correctamente.")
    else:
        print('El usuario no existe')

def BuscarEmpleados():
    verificar_archivo_vacio()
    IdMod=input('Digite el id que desea buscar: ')
    # Abrir el archivo JSON en modo lectura
    with open(archivo_empleados, "r") as archivo:
        contenido = json.load(archivo)  # Cargar el contenido actual del archivo
    
    if IdMod in contenido:
        empleado = contenido[IdMod]#primero llamo al empleado de empleados
        #ahi guardo el contenido referente al id
        print("Datos del empleado:")
        print("ID:", empleado["id"])
        print("Nombre:", empleado["nombre"])
        print("Horas trabajadas:", empleado["horas trabajadas"])
        print('Valor de la hora: {:,}'.format(int(empleado["valor hora"])))

    else:
        print('El usuario no existe')

def EliminarEmpleados():
    verificar_archivo_vacio()
    IdMod=input('Digite el id que desea buscar: ')
    # Abrir el archivo JSON en modo lectura
    with open(archivo_empleados, "r") as archivo:
        contenido = json.load(archivo)  # Cargar el contenido actual del archivo
    
    if IdMod in contenido:#si el id existe en algun contenido
        del contenido[IdMod]#con del eliminamos todo el contenido referente
        with open(archivo_empleados, "w") as archivo:
            json.dump(contenido, archivo)
        print("Empleado eliminado correctamente.")
    else:
        print('El usuario no existe')

def mostrarEmpleado():
    verificar_archivo_vacio()
    paginacion = 5#cinco como limite
    with open(archivo_empleados, "r") as archivo:
        contenido = json.load(archivo)  # Cargar el contenido actual del archivo
    total_empleados = len(contenido)#contamos cuantos empleados hay en total
    paginas = (total_empleados + paginacion - 1) // paginacion  # calculo del número de páginas

    pagina_actual = 1
    while True:
        inicio = (pagina_actual - 1) * paginacion
        fin = inicio + paginacion
        empleados_pagina = list(contenido.values())[inicio:fin]

        print("=== Empleados (Página", pagina_actual, "de", paginas, ") ===")
        for empleado in empleados_pagina:
            print("ID:", empleado["id"])
            print("Nombre:", empleado["nombre"])
            print("Horas trabajadas:", empleado["horas trabajadas"])
            print('Valor de la hora: {:,}'.format(int(empleado["valor hora"])))
            print('-'*40)

        if pagina_actual < paginas:
            opcion = input("Presione Enter para ver la siguiente página o ingrese 'M' para volver al menú: ")
            if opcion.upper() == "M":
                break
            pagina_actual += 1
        else:
            print("No hay más empleados para mostrar.")
            break

def ListarNominaEmpleado():
    verificar_archivo_vacio()
    id_empleado = input("Ingrese el ID del empleado para ver la nómina: ")
    with open(archivo_empleados, "r") as archivo:
        contenido = json.load(archivo)  # Cargar el contenido actual del archivo
    if id_empleado in contenido:
        empleado = contenido[id_empleado]
        salario_bruto = empleado["horas trabajadas"] * empleado["valor hora"]
        salario_minimo = 908526  # Salario mínimo legal vigente en Colombia 2023 (fuente: Ministerio del Trabajo)
        subsidio_transporte = 106454  # Valor del subsidio de transporte en Colombia 2023
        descuento_eps = salario_bruto * 0.04
        descuento_pension = salario_bruto * 0.04
        salario_neto = salario_bruto - descuento_eps - descuento_pension

        print("=== Nómina del empleado ===")
        print("ID:", id_empleado)
        print("Nombre:", empleado["nombre"])
        print("Horas trabajadas:", empleado["horas trabajadas"])
        print('Valor de la hora: {:,}'.format(int(empleado["valor hora"])))
        print("Salario bruto: {:,}".format(int(salario_bruto)))

        if salario_bruto < salario_minimo:
            print("Subsidio de transporte:", subsidio_transporte)

        print("Descuento EPS: {:,}".format(int(descuento_eps)))
        print("Descuento pensión: {:,}".format(int(descuento_pension)))
        print("Salario neto: {:,}".format(int(salario_neto)))

    else:
        print("El empleado no ha sido ingresado.")

def ListarNominaEmpleados():
    verificar_archivo_vacio()
    paginacion = 5#cinco como limite
    with open(archivo_empleados, "r") as archivo:
        contenido = json.load(archivo)  # Cargar el contenido actual del archivo
    total_empleados = len(contenido)#contamos cuantos empleados hay en total
    paginas = (total_empleados + paginacion - 1) // paginacion  # calculo del número de páginas

    pagina_actual = 1
    while True:
        inicio = (pagina_actual - 1) * paginacion
        fin = inicio + paginacion
        empleados_pagina = list(contenido.values())[inicio:fin]

        print("=== Empleados (Página", pagina_actual, "de", paginas, ") ===")
        for empleado in empleados_pagina:
            empleado = contenido[empleado['id']]
            salario_bruto = empleado["horas trabajadas"] * empleado["valor hora"]
            salario_minimo = 908526  # Salario mínimo legal vigente en Colombia 2023 (fuente: Ministerio del Trabajo)
            subsidio_transporte = 106454  # Valor del subsidio de transporte en Colombia 2023
            descuento_eps = salario_bruto * 0.04
            descuento_pension = salario_bruto * 0.04
            salario_neto = salario_bruto - descuento_eps - descuento_pension

            print("=== Nómina del empleado ===")
            print("ID:", empleado['id'])
            print("Nombre:", empleado["nombre"])
            print("Horas trabajadas:", empleado["horas trabajadas"])
            print('Valor de la hora: {:,}'.format(int(empleado["valor hora"])))
            print("Salario bruto: {:,}".format(int(salario_bruto)))

            if salario_bruto < salario_minimo:
                print("Subsidio de transporte:", subsidio_transporte)

            print("Descuento EPS: {:,}".format(int(descuento_eps)))
            print("Descuento pensión: {:,}".format(int(descuento_pension)))
            print("Salario neto: {:,}".format(int(salario_neto)))

        if pagina_actual < paginas:
            opcion = input("Presione Enter para ver la siguiente página o ingrese 'M' para volver al menú: ")
            if opcion.upper() == "M":
                break
            pagina_actual += 1
        else:
            print("No hay más empleados para mostrar.")
            break

def Menu():
    
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

crear_archivo_json()
Menu()