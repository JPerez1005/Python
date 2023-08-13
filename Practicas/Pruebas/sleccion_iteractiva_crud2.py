import curses

def agregar_estudiante(estudiantes, screen):
    screen.clear()#limpiamos pantalla
    screen.addstr(0, 0, 'Mi programa - Agregar Estudiante', curses.A_BOLD)# type: ignore
    screen.addstr(2, 0, "Ingrese el código del estudiante: ")#mostramos en pantalla
    curses.echo()# type: ignore | VER EN PANTALLA lo que se digita
    codigo = ""
    while True:
        input_str = screen.getstr(3, 0, 10).decode(encoding="utf-8")
        if input_str.isdigit():#si realmente es un numero
            codigo = input_str#se remplazan los valores
            screen.addstr(0, 0, " " * 46)  # Borra la línea
            break
        else:
            screen.addstr(3, 0, " " * 10)  # Borra la línea
            screen.addstr(0, 0, "INGRESE SOLO NÚMEROS. Inténtelo nuevamente.!!!")#atencion
            screen.refresh()# se hace un refresh actuando como continue
    screen.addstr(4, 0, "Ingrese el nombre completo del estudiante: ")
    screen.refresh()#actualizar pantalla
    nombre = ""
    while True:
        input_str = screen.getstr(5, 0, 100).decode(encoding="utf-8")
        if input_str.replace(" ", "").isalpha():#remplaza los espacios y a la vez verifica si son letras
            nombre = input_str#se remplazan los valores
            screen.addstr(0, 0, " " * 45)  # Borra la línea
            break
        else:
            screen.addstr(5, 0, " " * 100)  # Borra la línea
            screen.addstr(0, 0, "INGRESE SOLO LETRAS. Inténtelo nuevamente.!!!")#atencion
            screen.refresh()# se hace un refresh actuando como continue
    notas_parciales = []#se crea la lista de las notas
    for i in range(0,3,1):
        while True:
            screen.addstr(7 + i, 0, f"Ingrese la nota parcial {i+1}: ")
            screen.refresh()
            nota = screen.getstr(7 + i, 27, 2).decode(encoding="utf-8")#es como un input
            try:
                nota = float(nota)#La nota se convierte en decimal
                if 0.0 <= nota <= 5.0:#si la nota esta entre 0 y 5 entonces...
                    screen.addstr(16, 0, " "*60)
                    notas_parciales.append(nota)#se agrega la nota a la lista
                    break
                else:
                    screen.addstr(16, 0, "Ingrese una nota válida (número entre 0.0 y 5.0)")
                    screen.addstr(7 + i, 27, " "*3)
                    screen.refresh()# si se hace un refresh es como hacer un continue
            except ValueError:#value error detecta si hay letras
                screen.addstr(16, 0, "Ingrese una nota válida (número entre 0.0 y 5.0)")
                screen.addstr(7 + i, 27, " "*3)
                screen.refresh()

    curses.noecho()# type: ignore | DEJAR DE VER EN PANTALLA los datos ingresados
    estudiantes[codigo] = {
        "nombre": nombre,
        "notas_parciales": notas_parciales,
        "nota_definitiva": sum(notas_parciales) / len(notas_parciales)
    }
    screen.addstr(16, 0, " "*60)
    screen.addstr(12, 0, "Registro agregado exitosamente.")
    screen.refresh()

def buscar_estudiante(estudiantes, screen):
    screen.clear()
    screen.addstr(0, 0, 'Mi programa - Buscar Estudiante', curses.A_BOLD)# type: ignore
    screen.addstr(2, 0, "Ingrese el código del estudiante a buscar: ")
    screen.refresh()
    curses.echo()# type: ignore
    codigo = screen.getstr(3, 0, 10).decode(encoding="utf-8")
    curses.noecho()# type: ignore

    if codigo in estudiantes:
        estudiante = estudiantes[codigo]
        screen.addstr(5, 0, "Estudiante encontrado:")
        screen.addstr(7, 0, f"Nombre completo: {estudiante['nombre']}")
        screen.addstr(8, 3, "+"+"-" * 35+"+")
        screen.addstr(9, 3, "|{:^11}|{:^14}|{:^8}|".format("CODIGO", "NOTAS", "PROMEDIO"))
        screen.addstr(10, 3, "-"*37)
        notas_parciales_str = ", ".join(map(str, estudiante['notas_parciales']))
        screen.addstr(11, 3, "|{:<11}|{:<14}|{:<8.1f}|".format(codigo, notas_parciales_str, estudiante['nota_definitiva']))
        screen.addstr(12, 3, "+"+"-" * 35+"+")
    else:
        screen.addstr(5, 0, f"No se encontró un estudiante con el código: {codigo}")
    
    screen.refresh()

def cambiar_nombre_estudiante(estudiantes, screen):
    screen.clear()#limpiamos pantalla
    screen.addstr(0, 0, 'Mi programa - Cambiar Nombre Del Estudiante', curses.A_BOLD)# type: ignore
    screen.addstr(1, 0, "Digite cero para salir!!")#mostramos en pantalla
    screen.addstr(2, 0, "Ingrese el código del estudiante: ")#mostramos en pantalla
    curses.echo()# type: ignore | VER EN PANTALLA lo que se digita
    codigo = ""
    while True:
        input_str = screen.getstr(3, 0, 10).decode(encoding="utf-8")
        if input_str.isdigit():#si realmente es un numero
            codigo = input_str#se remplazan los valores
            screen.addstr(0, 0, " " * 46)  # Borra la línea
            break
        else:
            screen.addstr(3, 0, " " * 10)  # Borra la línea
            screen.addstr(0, 0, "INGRESE SOLO NÚMEROS. Inténtelo nuevamente.!!!")#atencion
            screen.refresh()# se hace un refresh actuando como continue
    if codigo in estudiantes:
        screen.addstr(1, 0, " "*30)#mostramos en pantalla
        screen.addstr(5, 0, "El estudiante está registrado...")#atencion
        screen.addstr(6, 0, "Ingrese el nombre completo del estudiante a cambiar: ")
        screen.refresh()#actualizar pantalla
        nombre = ""
        while True:
            input_str = screen.getstr(7, 0, 100).decode(encoding="utf-8")
            if input_str.replace(" ", "").isalpha():#remplaza los espacios y a la vez verifica si son letras
                nombre = input_str#se remplazan los valores
                screen.addstr(0, 0, " " * 45)  # Borra la línea
                estudiantes[codigo] = {
                    "nombre": nombre,
                    "notas_parciales": estudiantes[codigo]['notas_parciales'],
                    "nota_definitiva": estudiantes[codigo]['nota_definitiva']
                }
                break
            else:
                screen.addstr(7, 0, " " * 100)  # Borra la línea
                screen.addstr(0, 0, "INGRESE SOLO LETRAS. Inténtelo nuevamente.!!!")#atencion
                screen.refresh()# se hace un refresh actuando como continue
    elif codigo==0:
        return
    else:
        screen.addstr(5, 0, "El estudiante no está registrado...")#atencion
        screen.refresh()# se hace un refresh actuando como continue
    curses.noecho()# type: ignore | Ya no se ve EN PANTALLA lo que se digita

def cambiar_notas_estudiante(estudiantes, screen):
    screen.clear()#limpiamos pantalla
    screen.addstr(0, 0, 'Mi programa - Cambiar Notas Del Estudiante', curses.A_BOLD)# type: ignore
    screen.addstr(1, 0, "Digite cero para salir!!")#mostramos en pantalla
    screen.addstr(2, 0, "Ingrese el código del estudiante: ")#mostramos en pantalla
    curses.echo()# type: ignore | VER EN PANTALLA lo que se digita
    codigo = ""
    while True:
        input_str = screen.getstr(3, 0, 10).decode(encoding="utf-8")
        if input_str.isdigit():#si realmente es un numero
            codigo = input_str#se remplazan los valores
            screen.addstr(0, 0, " " * 46)  # Borra la línea
            break
        else:
            screen.addstr(3, 0, " " * 10)  # Borra la línea
            screen.addstr(0, 0, "INGRESE SOLO NÚMEROS. Inténtelo nuevamente.!!!")#atencion
            screen.refresh()# se hace un refresh actuando como continue
    if codigo in estudiantes:
        screen.addstr(1, 0, " "*30)#mostramos en pantalla
        screen.addstr(5, 0, "El estudiante está registrado...")#atencion
        screen.addstr(6, 0, "Ingrese las notas del estudiante a cambiar: ")
        screen.refresh()#actualizar pantalla
        
        notas_parciales = []#se crea la lista de las notas
        for i in range(3):
            while True:
                screen.addstr(7 + i, 0, f"Ingrese la nota parcial {i+1}: ")
                screen.refresh()
                nota = screen.getstr(8 + i, 0, 10).decode(encoding="utf-8")#es como un input
                try:
                    screen.addstr(0, 0, " " * 45)  # Borra la línea
                    nota = float(nota)#La nota se convierte en decimal
                    if 0.0 <= nota <= 5.0:#si la nota esta entre 0 y 5 entonces...
                        notas_parciales.append(nota)#se agrega la nota a la lista
                        break
                    else:
                        screen.addstr(10 + i, 0, "Ingrese una nota válida (número entre 0.0 y 5.0)")
                        screen.refresh()# si se hace un refresh es como hacer un continue
                except ValueError:#value error detecta si hay letras
                    screen.addstr(10 + i, 0, "Ingrese una nota válida (número entre 0.0 y 5.0)")
                    screen.refresh()
            
            estudiantes[codigo] = {
                "nombre": estudiantes[codigo]['nombre'],
                "notas_parciales": notas_parciales,
                "nota_definitiva": sum(notas_parciales) / len(notas_parciales)
            }
    elif codigo==0:
        return
    else:
        screen.addstr(5, 0, "El estudiante no está registrado...")#atencion
        screen.refresh()# se hace un refresh actuando como continue
    curses.noecho()# type: ignore | Ya no se ve EN PANTALLA lo que se digita

def actualizar_estudiante(estudiantes, screen):
    
    curses.start_color()# type: ignore
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)# type: ignore
    
    screen.clear()
    screen.refresh()
    
    options = ['Cambiar Nombre del estudiante.', 'Cambiar notas del estudiante.', 'Ir a Menú Principal.']
    selection=0
    
    while True:
        screen.clear()
        screen.addstr(0, 0, 'Mi programa - Cambiar Datos de Usuario', curses.A_BOLD)# type: ignore
        
        for i, option in enumerate(options):#SELECTOR
            if i == selection:
                screen.addstr(i+2, 5, option, curses.color_pair(1))# type: ignore
            else:
                screen.addstr(i+2, 5, option)
                
        key = screen.getch()
                
        if key == curses.KEY_UP and selection > 0:# type: ignore
            selection -= 1
        elif key == curses.KEY_DOWN and selection < len(options)-1:# type: ignore
            selection += 1
        elif key == 10: # si el usuario presiona Enter entonces...
            if selection == len(options)-1:#si es la ultima opcion
                break
            elif selection == 0:
                cambiar_nombre_estudiante(estudiantes, screen)  # Llamar a la función para agregar un estudiante
                screen.addstr(len(options)+13, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            elif selection == 1:
                cambiar_notas_estudiante(estudiantes, screen)
                screen.addstr(len(options)+13, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            elif selection == 2:
                return

def borrar_estudiante(estudiantes, screen):
    screen.clear()#limpiamos pantalla
    screen.addstr(0, 0, 'Mi programa - Delete Student', curses.A_BOLD)# type: ignore
    screen.addstr(1, 0, "Digite cero para salir!!")#mostramos en pantalla
    screen.addstr(2, 0, "Ingrese el código del estudiante a eliminar: ")#mostramos en pantalla
    curses.echo()# type: ignore | VER EN PANTALLA lo que se digita
    codigo = ""
    while True:
        input_str = screen.getstr(3, 0, 10).decode(encoding="utf-8")
        if input_str.isdigit():#si realmente es un numero
            codigo = input_str#se remplazan los valores
            screen.addstr(0, 0, " " * 46)  # Borra la línea
            break
        else:
            screen.addstr(3, 0, " " * 10)  # Borra la línea
            screen.addstr(0, 0, "INGRESE SOLO NÚMEROS. Inténtelo nuevamente.!!!")#atencion
            screen.refresh()# se hace un refresh actuando como continue
    if codigo in estudiantes:
        screen.addstr(1, 0, " "*30)#mostramos en pantalla
        screen.addstr(5, 0, "El estudiante está registrado...")#mensaje validado...
        del estudiantes[codigo]
        screen.addstr(7, 0, "Ya no :)")#mensaje
    elif codigo=='0':
        screen.addstr(7, 0, "Saliendo :)")#mensaje
    else:
        screen.addstr(5, 0, "No existe algún estudiante con ese codigo...")#atencion
    pass

def listar_estudiantes(estudiantes, screen):
    screen.clear()
    screen.addstr(0, 0, 'Mi programa - Lista de Estudiantes', curses.A_BOLD)# type: ignore
    if not estudiantes:
        screen.addstr(2, 0, "No hay estudiantes registrados.")
    else:
        rta=True
        for estudiante in estudiantes.values():
            if len(estudiante['nombre'])<30:
                rta=True
            else:
                rta=False
                break
        
        if rta==True:
            screen.addstr(1, 0, "+"+"-" * 66+"+")
            screen.addstr(2, 0, "|{:<11}|{:<30}|{:<14}|{:<8}|".format("CODIGO", "NOMBRE", "NOTAS", "PROMEDIO"))
            screen.addstr(3, 0, "+"+"-" * 66+"+")
            i=4
            for codigo, estudiante in estudiantes.items():
                notas_parciales_str = ", ".join(map(str, estudiante['notas_parciales']))
                screen.addstr(i, 0,"|{:<11}|{:<30}|{:<14}|{:<8.1f}|".format(codigo, estudiante['nombre'], notas_parciales_str, estudiante['nota_definitiva']))
                i+=1
            screen.addstr(i, 0, "+"+"-" * 66+"+")
            screen.addstr(i+5, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
            screen.getch()
        else:
            screen.addstr(1, 0, "+"+"-" * 86+"+")
            screen.addstr(2, 0, "|{:<11}|{:<50}|{:<14}|{:<8}|".format("CODIGO", "NOMBRE", "NOTAS", "PROMEDIO"))
            screen.addstr(3, 0, "+"+"-" * 86+"+")
            i=4
            for codigo, estudiante in estudiantes.items():
                notas_parciales_str = ", ".join(map(str, estudiante['notas_parciales']))
                screen.addstr(i, 0,"|{:<11}|{:<50}|{:<14}|{:<8.1f}|".format(codigo, estudiante['nombre'], notas_parciales_str, estudiante['nota_definitiva']))
                i+=1
            screen.addstr(i, 0, "+"+"-" * 86+"+")
            screen.addstr(i+5, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
            screen.getch()
    screen.refresh()

def show_menu(screen):
    estudiantes = {}
    curses.start_color()# type: ignore
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)# type: ignore
    
    screen.clear()
    screen.refresh()
    
    options = ['Agregar un nuevo registro.', 'Buscar un Estudiante.', 'Actualizar datos del Estudiante.', 'Borrar Estudiante.', 'Listar Estudiantes.', 'Salir.']
    selection = 0
    
    while True:
        screen.clear()
        screen.addstr(0, 0, 'Mi programa - Menú Principal', curses.A_BOLD)# type: ignore
        
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
        elif key == 10: # si el usuario presiona Enter entonces...
            if selection == len(options)-1:#si es la ultima opcion
                break
            elif selection == 0:
                agregar_estudiante(estudiantes, screen)  # Llamar a la función para agregar un estudiante
                screen.addstr(len(options)+13, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            elif selection == 1:
                buscar_estudiante(estudiantes, screen)
                screen.addstr(len(options)+13, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            elif selection == 2:
                actualizar_estudiante(estudiantes, screen)
            elif selection == 3:
                borrar_estudiante(estudiantes, screen)
                screen.addstr(len(options)+13, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            elif selection == 4:
                listar_estudiantes(estudiantes, screen)
                

curses.wrapper(show_menu)# type: ignore
