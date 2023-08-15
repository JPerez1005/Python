import curses#se hace la importacion de curses

def integer_validation(entrance, screen, f1, c1):
    curses.echo()# type: ignore | see on screen what is being typed
    while True:
        input_str = screen.getstr(f1, 0, 10).decode(encoding="utf-8")
        if input_str.isdigit():#si realmente es un numero
            entrance = input_str#se remplazan los valores
            screen.addstr(f1+10, c1, " " * 46)  # Borra la línea
            return entrance
        else:
            screen.addstr(f1, c1, " " * 10)  # Borra la línea
            screen.addstr(f1+10, c1, "INGRESE SOLO NÚMEROS. Inténtelo nuevamente.!!!")#atencion
            screen.refresh()# se hace un refresh actuando como continue
    curses.noecho()# type: ignore | stop seeing on the screen what is being typed

def string_validation(entrance, screen, f1, c1):
    curses.echo()# type: ignore | see on screen what is being typed
    while True:
        input_str = screen.getstr(f1, c1, 100).decode(encoding="utf-8")
        if input_str.replace(" ", "").isalpha():#remplaza los espacios y a la vez verifica si son letras
            entrance = input_str#se remplazan los valores
            screen.addstr(f1+10, c1, " " * 45)  # Borra la línea
            return entrance
        else:
            screen.addstr(f1, c1, " " * 100)  # Borra la línea
            screen.addstr(f1+10, c1, "INGRESE SOLO LETRAS. Inténtelo nuevamente.!!!")#atencion
            screen.refresh()# we do a refresh acting like a continue
    curses.noecho()# type: ignore | stop seeing on the screen what is being typed

def cargar_empleados():
    # Carga la información de empleados desde el archivo emplacme.dat
    empleados = {}
    try:#Usamos un bloque try-except para manejar el caso en que el archivo "emplacme.dat" no existe
        with open("emplacme.dat", "r") as archivo:#abrimos el archivo en modo lectura
            lineas = archivo.readlines()#leemos todas las lineas y la almacenamos en lineas
            encabezados = lineas[0].strip().split(";")#a la primera linea le hacemos el encabezado
            for linea in lineas[1:]:#para cada linea desde la linea 2 hacia delante
                datos = linea.strip().split(";")# se lee cada linea y se almacena
                empleado = {}#se crea un diccionario de empleado para almacenar datos de un empleado
                for i, encabezado in enumerate(encabezados):
                    empleado[encabezado] = datos[i]
                empleados[empleado["id"]] = empleado
    except FileNotFoundError:#(es la primera vez que se ejecuta el programa o el archivo no está presente).
        pass
    return empleados

def guardar_empleados(empleados):
    # Guarda la información de empleados en el archivo emplacme.dat
    encabezados = "id;nombre;horas_trabajadas;valor_hora\n"
    datos_empleados = [encabezados]
    for empleado in empleados.values():
        datos_empleado = [empleado["id"], empleado["nombre"], empleado["horas_trabajadas"], empleado["valor_hora"]]
        datos_empleados.append(";".join(datos_empleado) + "\n")
    with open("emplacme.dat", "w") as archivo:
        archivo.writelines(datos_empleados)

def agregar_empleado(empleados, screen):
    screen.clear()
    screen.addstr(1, 0, "Agregar nuevo empleado")
    
    # Capturar el ID del empleado (validar que sea un número entero)
    while True:
        screen.addstr(3, 0, "Ingrese el ID del empleado: ")
        screen.refresh()
        codigo = integer_validation("", screen, 4, 0)# type: ignore
        if codigo not in empleados:
            break
        else:
            screen.addstr(0, 0, "Este ID ya está en uso. Ingrese un ID único.")# type: ignore
            screen.refresh()
            screen.addstr(4, 0, " "*10)
    
    # Capturar el nombre del empleado (validar que sean letras)
    screen.addstr(6, 0, "Ingrese el nombre del empleado: ")
    screen.refresh()
    nombre = string_validation("", screen, 7, 0)# type: ignore
    
    # Capturar las horas trabajadas (validar que sean números enteros)
    screen.addstr(8, 0, "Ingrese las horas trabajadas: ")
    screen.refresh()
    horas_trabajadas = integer_validation("", screen, 9, 0)# type: ignore
    
    # Capturar el valor de la hora (validar que sea un número)
    screen.addstr(10, 0, "Ingrese el valor de la hora: ")
    screen.refresh()
    valor_hora = integer_validation("", screen, 11, 0)
    entrance=int(valor_hora)# type: ignore
    while True:
        if 8000<entrance<150000:
            screen.addstr(12, 0, "Valor de Hora Valida.")
            break
        else:
            screen.addstr(12, 0, 'Valor de Hora no Valida')
            screen.refresh()
    # Agregar el empleado al diccionario
    empleados[codigo] = {
        "id": codigo,
        "nombre": nombre,
        "horas_trabajadas": horas_trabajadas,
        "valor_hora": valor_hora
    }
    
    screen.addstr(15, 0, "Empleado agregado exitosamente.")
    screen.refresh()
    screen.getch()


def modificar_empleado(empleados, screen):
    # Función para modificar un empleado existente
    # Implementa la lógica de búsqueda y modificación de empleados
    pass

# Función para buscar un empleado
# Implementa la lógica para buscar un empleado por su id o nombre

# Función para eliminar un empleado
# Implementa la lógica para eliminar un empleado

def listar_empleados(empleados, screen):
    screen.clear()
    screen.addstr(0, 0, 'NÓMINA ACME - Listar Empleados', curses.A_BOLD)# type: ignore

    empleados_list = list(empleados.values())
    total_empleados = len(empleados_list)
    empleados_por_pagina = 5
    pagina_actual = 0

    while pagina_actual * empleados_por_pagina < total_empleados:
        pantalla_vacia = True

        for i in range(pagina_actual * empleados_por_pagina, (pagina_actual + 1) * empleados_por_pagina):
            if i < total_empleados:
                empleado = empleados_list[i]
                screen.addstr(3 + (i % empleados_por_pagina), 0, f"ID: {empleado['id']},\
                    Nombre: {empleado['nombre']}, Horas Trabajadas: {empleado['horas_trabajadas']},\
                    Valor Hora: {empleado['valor_hora']}")
                pantalla_vacia = False

        if pantalla_vacia:
            break

        screen.addstr(9, 0, "Presiona 'Enter' para ver más empleados, o 'M' para volver al Menú Principal...")
        screen.refresh()

        key = screen.getch()

        if key == ord('\n'):
            pagina_actual += 1
            screen.clear()
            screen.addstr(0, 0, 'NÓMINA ACME - Listar Empleados', curses.A_BOLD)# type: ignore
        elif key == ord('M') or key == ord('m'):
            break

    screen.clear()
    screen.addstr(0, 0, 'Operación completada exitosamente. Presiona Enter para continuar...',)# type: ignore
    screen.refresh()
    screen.getch()


def calcular_nomina(empleado, valor_hora, salario_minimo):
    horas_trabajadas = float(empleado['horas_trabajadas'])
    valor_hora = float(empleado['valor_hora'])
    salario_bruto = horas_trabajadas * valor_hora
    if salario_bruto < salario_minimo:
        subsidio_transporte = 102854 # Valor del subsidio de transporte en 2023
    else:
        subsidio_transporte = 0
    descuento_eps = salario_bruto * 0.04
    descuento_pension = salario_bruto * 0.04
    salario_neto = salario_bruto + subsidio_transporte - descuento_eps - descuento_pension

    return {
        "salario_bruto": salario_bruto,
        "subsidio_transporte": subsidio_transporte,
        "descuento_eps": descuento_eps,
        "descuento_pension": descuento_pension,
        "salario_neto": salario_neto
    }

def listar_nomina_empleado(empleados, screen):
    screen.clear()
    screen.addstr(0, 0, 'Mi programa - Listar Nómina de Empleado', curses.A_BOLD)#type:ignore
    screen.addstr(2, 0, "Ingrese el ID del empleado para listar la nómina: ")
    screen.refresh()

    id_empleado = integer_validation("", screen, 3, 0)
    # Valor del salario mínimo en Colombia para 2023
    salario_minimo = 996280
    if id_empleado in empleados:
        empleado = empleados[id_empleado]
        nomina = calcular_nomina(empleado, empleado['valor_hora'], salario_minimo)

        screen.addstr(5, 0, f"ID del empleado: {id_empleado}")
        screen.addstr(6, 0, f"Nombre del empleado: {empleado['nombre']}")
        screen.addstr(7, 0, f"Horas trabajadas: {empleado['horas_trabajadas']}")
        screen.addstr(8, 0, f"Valor de la hora: {empleado['valor_hora']}")
        screen.addstr(10, 0, "Nómina:")
        screen.addstr(11, 0, f"Salario bruto: {nomina['salario_bruto']}")
        screen.addstr(12, 0, f"Subsidio de transporte: {nomina['subsidio_transporte']}")
        screen.addstr(13, 0, f"Descuento EPS: {nomina['descuento_eps']}")
        screen.addstr(14, 0, f"Descuento Pensión: {nomina['descuento_pension']}")
        screen.addstr(15, 0, f"Salario neto: {nomina['salario_neto']}")
    else:
        screen.addstr(5, 0, f"No se encontró un empleado con el ID: {id_empleado}")

    screen.refresh()


# Función para listar la nómina de todos los empleados
# Implementa la lógica para mostrar la nómina de todos los empleados

def show_menu(screen):
    empleados = cargar_empleados()
    curses.start_color()# type: ignore
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)# type: ignore
    
    options = ['1- Agregar empleado', '2- Modificar empleado', '3- Buscar empleado',
               '4- Eliminar empleado', '5- Listar empleados', '6- Listar nómina de un empleado',
               '7- Listar nómina de todos los empleados', '8- Salir']
    selection = 0
    
    while True:
        screen.clear()
        screen.refresh()
        screen.addstr(0, 0, '*** NOMINA ACME ***', curses.A_BOLD)# type: ignore
        
        for i, option in enumerate(options):
            if i == selection:
                screen.addstr(i+2, 5, option, curses.color_pair(1))# type: ignore
            else:
                screen.addstr(i+2, 5, option)
        
        key = screen.getch()
        
        if key == curses.KEY_UP and selection > 0:# type: ignore
            selection -= 1
        elif key == curses.KEY_DOWN and selection < len(options)-1:# type: ignore
            selection += 1
        elif key == 10:
            if selection == len(options)-1:
                guardar_empleados(empleados)
                break
            elif selection == 0:
                agregar_empleado(empleados, screen)
                screen.addstr(len(options)+10, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            elif selection == 1:
                modificar_empleado(empleados, screen)
                screen.addstr(len(options)+10, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            elif selection == 4:
                listar_empleados(empleados, screen)
                screen.addstr(len(options)+10, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            elif selection == 5:
                listar_nomina_empleado(empleados, screen)
                screen.addstr(len(options)+10, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            # Agrega el código para las otras opciones del menú
            pass

curses.wrapper(show_menu)# type: ignore
