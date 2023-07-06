import math
empleados = []

# Función para agregar un empleado
def agregar_empleado():
    id_empleado = input("Ingrese el ID del empleado: ")
    nombre = input("Ingrese el nombre del empleado: ")
    horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
    valor_hora = int(input("Ingrese el valor de la hora trabajada: "))

    empleado = [id_empleado, nombre, horas_trabajadas, valor_hora]
    empleados.append(empleado)

    print("Empleado agregado correctamente.")

# Función para modificar un empleado
def modificar_empleado():
    id_empleado = input("Ingrese el ID del empleado a modificar: ")

    for empleado in empleados:
        if empleado[0] == id_empleado:
            nombre = input("Ingrese el nuevo nombre del empleado: ")
            horas_trabajadas = int(input("Ingrese la nueva cantidad de horas trabajadas: "))
            valor_hora = int(input("Ingrese el nuevo valor de la hora trabajada: "))

            empleado[1] = nombre
            empleado[2] = horas_trabajadas
            empleado[3] = valor_hora

            print("Empleado modificado correctamente.")
            return

    print("No se encontró un empleado con el ID ingresado.")

# Función para buscar un empleado
def buscar_empleado():
    id_empleado = input("Ingrese el ID del empleado a buscar: ")

    for empleado in empleados:
        if empleado[0] == id_empleado:
            print("ID:", empleado[0])
            print("Nombre:", empleado[1])
            print("Horas trabajadas:", empleado[2])
            print("Valor de la hora:", empleado[3])
            return

    print("No se encontró un empleado con el ID ingresado.")

# Función para eliminar un empleado
def eliminar_empleado():
    id_empleado = input("Ingrese el ID del empleado a eliminar: ")

    for empleado in empleados:
        if empleado[0] == id_empleado:
            empleados.remove(empleado)
            print("Empleado eliminado correctamente.")
            return

    print("No se encontró un empleado con el ID ingresado.")

# Función para listar empleados
def listar_empleados():
    if len(empleados) == 0:
        print("No hay empleados registrados.")
        return

    num_empleados = len(empleados)
    tam_pagina = 5
    num_paginas = math.ceil(num_empleados / tam_pagina)
    pagina_actual = 1
    indice_inicial = 0

    while pagina_actual <= num_paginas:
        print("=== Página", pagina_actual, "===")
        empleados_pagina = empleados[indice_inicial:indice_inicial+tam_pagina]

        for empleado in empleados_pagina:
            print("ID:", empleado[0])
            print("Nombre:", empleado[1])
            print("Horas trabajadas:", empleado[2])
            print("Valor de la hora:", empleado[3])
            print("-------------------")

        if pagina_actual < num_paginas:
            respuesta = input("Presione Enter para ver los siguientes empleados o ingrese 'M' para volver al menú: ")
            if respuesta.lower() == "m":
                break

        pagina_actual += 1
        indice_inicial += tam_pagina

# Función para calcular la nómina de un empleado
def calcular_nomina_empleado():
    id_empleado = input("Ingrese el ID del empleado: ")

    for empleado in empleados:
        if empleado[0] == id_empleado:
            horas_trabajadas = empleado[2]
            valor_hora = empleado[3]
            salario_bruto = horas_trabajadas * valor_hora
            salario_minimo = 908526  # Salario mínimo legal vigente en Colombia para el año 2023
            auxilio_transporte = 106454  # Auxilio de transporte para el año 2023
            eps = salario_bruto * 0.04
            pension = salario_bruto * 0.04
            salario_neto = salario_bruto - eps - pension

            print("ID:", empleado[0])
            print("Nombre:", empleado[1])
            print("Horas trabajadas:", horas_trabajadas)
            print("Valor de la hora:", valor_hora)
            print("Salario bruto:", salario_bruto)
            if salario_bruto < salario_minimo:
                print("Auxilio de transporte:", auxilio_transporte)
            print("EPS:", eps)
            print("Pensión:", pension)
            print("Salario neto:", salario_neto)
            print("-------------------")

            return

    print("No se encontró un empleado con el ID ingresado.")

# Función para listar la nómina de todos los empleados
def listar_nomina_empleados():
    if len(empleados) == 0:
        print("No hay empleados registrados.")
        return

    num_empleados = len(empleados)
    tam_pagina = 5
    num_paginas = math.ceil(num_empleados / tam_pagina)
    pagina_actual = 1
    indice_inicial = 0

    while pagina_actual <= num_paginas:
        print("=== Página", pagina_actual, "===")
        empleados_pagina = empleados[indice_inicial:indice_inicial+tam_pagina]

        for empleado in empleados_pagina:
            print("ID:", empleado[0])
            print("Nombre:", empleado[1])
            horas_trabajadas = empleado[2]
            valor_hora = empleado[3]
            salario_bruto = horas_trabajadas * valor_hora
            salario_minimo = 908526  # Salario mínimo legal vigente en Colombia para el año 2023
            auxilio_transporte = 106454  # Auxilio de transporte para el año 2023
            eps = salario_bruto * 0.04
            pension = salario_bruto * 0.04
            salario_neto = salario_bruto - eps - pension

            print("Salario bruto:", salario_bruto)
            if salario_bruto < salario_minimo:
                print("Auxilio de transporte:", auxilio_transporte)
            print("EPS:", eps)
            print("Pensión:", pension)
            print("Salario neto:", salario_neto)
            print("-------------------")

        if pagina_actual < num_paginas:
            respuesta = input("Presione Enter para ver los siguientes empleados o ingrese 'M' para volver al menú: ")
            if respuesta.lower() == "m":
                break

        pagina_actual += 1
        indice_inicial += tam_pagina

# Función principal del programa
def main():
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
            calcular_nomina_empleado()
        elif opcion == "7":
            listar_nomina_empleados()
        elif opcion == "8":
            confirmacion = input("¿Está seguro de que desea salir? (S/N): ")
            if confirmacion.lower() == "s":
                print("Gracias por utilizar el programa. ¡Hasta luego!")
                break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

# Ejecutar el programa
main()
