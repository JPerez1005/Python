# Diccionario para almacenar los empleados y sus datos
empleados = {}

def agregar_empleado():
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
    print("Empleado agregado correctamente.")

def modificar_empleado():
    id_empleado = input("Ingrese el ID del empleado a modificar: ")
    if id_empleado not in empleados:
        print("El ID del empleado no existe. Use la opción 'Agregar empleado' para crear un nuevo empleado.")
        return
    
    # Solicitar los nuevos datos del empleado
    nombre = input("Ingrese el nuevo nombre del empleado: ")
    horas_trabajadas = int(input("Ingrese la nueva cantidad de horas trabajadas: "))
    valor_hora = float(input("Ingrese el nuevo valor de la hora trabajada: "))

    # Actualizar los datos del empleado en el diccionario
    empleados[id_empleado]["nombre"] = nombre
    empleados[id_empleado]["horas_trabajadas"] = horas_trabajadas
    empleados[id_empleado]["valor_hora"] = valor_hora
    print("Empleado modificado correctamente.")

def buscar_empleado():
    id_empleado = input("Ingrese el ID del empleado a buscar: ")
    if id_empleado in empleados:
        empleado = empleados[id_empleado]
        print("Información del empleado:")
        print("ID:", id_empleado)
        print("Nombre:", empleado["nombre"])
        print("Horas trabajadas:", empleado["horas_trabajadas"])
        print("Valor de la hora:", empleado["valor_hora"])
    else:
        print("El empleado no ha sido ingresado.")

def eliminar_empleado():
    id_empleado = input("Ingrese el ID del empleado a eliminar: ")
    if id_empleado in empleados:
        del empleados[id_empleado]
        print("Empleado eliminado correctamente.")
    else:
        print("No se encontró ningún empleado con ese ID.")

def listar_empleados():
    paginacion = 5#cinco como limite
    total_empleados = len(empleados)#contamos cuantos empleados hay en total
    paginas = (total_empleados + paginacion - 1) // paginacion  # calculo del número de páginas

    pagina_actual = 1
    while True:
        inicio = (pagina_actual - 1) * paginacion
        fin = inicio + paginacion
        empleados_pagina = list(empleados.values())[inicio:fin]

        print("=== Empleados (Página", pagina_actual, "de", paginas, ") ===")
        for empleado in empleados_pagina:
            print("ID:", empleado['id'])
            print("Nombre:", empleado["nombre"])
            print("Horas trabajadas:", empleado["horas_trabajadas"])
            print("Valor de la hora:", empleado["valor_hora"])
            print('-'*40)

        if pagina_actual < paginas:
            opcion = input("Presione Enter para ver la siguiente página o ingrese 'M' para volver al menú: ")
            if opcion.upper() == "M":
                break
            pagina_actual += 1
        else:
            print("No hay más empleados para mostrar.")
            break

def listar_nomina_empleado():
    id_empleado = input("Ingrese el ID del empleado para ver la nómina: ")
    if id_empleado in empleados:
        empleado = empleados[id_empleado]
        salario_bruto = empleado["horas_trabajadas"] * empleado["valor_hora"]
        salario_minimo = 908526  # Salario mínimo legal vigente en Colombia 2023 (fuente: Ministerio del Trabajo)
        subsidio_transporte = 106454  # Valor del subsidio de transporte en Colombia 2023
        descuento_eps = salario_bruto * 0.04
        descuento_pension = salario_bruto * 0.04
        salario_neto = salario_bruto - descuento_eps - descuento_pension

        print("=== Nómina del empleado ===")
        print("ID:", id_empleado)
        print("Nombre:", empleado["nombre"])
        print("Horas trabajadas:", empleado["horas_trabajadas"])
        print("Valor de la hora:", empleado["valor_hora"])
        print("Salario bruto:", salario_bruto)

        if salario_bruto < salario_minimo:
            print("Subsidio de transporte:", subsidio_transporte)

        print("Descuento EPS:", descuento_eps)
        print("Descuento pensión:", descuento_pension)
        print("Salario neto:", salario_neto)

    else:
        print("El empleado no ha sido ingresado.")

def listar_nomina_empleados():
    paginacion = 5
    total_empleados = len(empleados)
    paginas = (total_empleados + paginacion - 1) // paginacion  # Cálculo del número de páginas

    pagina_actual = 1
    while True:
        inicio = (pagina_actual - 1) * paginacion
        fin = inicio + paginacion
        empleados_pagina = list(empleados.values())[inicio:fin]

        print("=== Nómina de Empleados (Página", pagina_actual, "de", paginas, ") ===")
        for empleado in empleados_pagina:
            salario_bruto = empleado["horas_trabajadas"] * empleado["valor_hora"]
            salario_minimo = 908526  # Salario mínimo legal vigente en Colombia 2023 (fuente: Ministerio del Trabajo)
            subsidio_transporte = 106454  # Valor del subsidio de transporte en Colombia 2023
            descuento_eps = salario_bruto * 0.04
            descuento_pension = salario_bruto * 0.04
            salario_neto = salario_bruto - descuento_eps - descuento_pension

            print("ID:", empleado["id"])
            print("Nombre:", empleado["nombre"])
            print("Horas trabajadas:", empleado["horas_trabajadas"])
            print("Valor de la hora:", empleado["valor_hora"])
            print("Salario bruto:", salario_bruto)

            if salario_bruto < salario_minimo:
                print("Subsidio de transporte:", subsidio_transporte)

            print("Descuento EPS:", descuento_eps)
            print("Descuento pensión:", descuento_pension)
            print("Salario neto:", salario_neto)
            print("--------------------")

        if pagina_actual < paginas:
            opcion = input("Presione Enter para ver la siguiente página o ingrese 'M' para volver al menú: ")
            if opcion.upper() == "M":
                break
            pagina_actual += 1
        else:
            print("No hay más empleados para mostrar.")
            break

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
            agregar_empleado()
        elif opcion == "2":
            modificar_empleado()
        elif opcion == "3":
            buscar_empleado()
        elif opcion == "4":
            eliminar_empleado()
        elif opcion == "5":
            listar_empleados()
        elif opcion == "6":
            listar_nomina_empleado()
        elif opcion == "7":
            listar_nomina_empleados()
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