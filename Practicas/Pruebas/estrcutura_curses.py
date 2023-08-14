import curses

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

def function1(my_dictionary,screen):
    #WE CAN CLEAR AND UPDATE THE SCREEN------------------------------------------
    screen.clear()
    screen.refresh()
    screen.addstr(1, 0, "Ingrese el nombre completo del usuario: ")
    screen.refresh()#actualizar pantalla
    nombre = ""
    entrance=string_validation(nombre, screen, 2, 0)
    my_dictionary['nombre']=entrance

def function2(my_dictionary,screen):
    screen.clear()#limpiamos pantalla
    screen.addstr(1, 0, "Ingrese el código del estudiante: ")#mostramos en pantalla
    codigo = ""
    entrance=integer_validation(codigo, screen, 2, 0)
    my_dictionary['codigo']=entrance

def function3(my_dictionary,screen):
    screen.clear()#limpiamos pantalla
    screen.addstr(1, 0, f'Nombre: {my_dictionary["nombre"]}')#show on screen
    screen.addstr(2, 0, f'Codigos: {my_dictionary["codigo"]}')#show on screen

def show_menu(screen):
    #CREATE A DICTIONARY---------------------------------------------------------
    my_dictionary = {}#if a dictionary is used, this is the best time to call it
    
    #WE CAN CHOOSE THE COLORS----------------------------------------------------
    curses.start_color()# type: ignore
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)# type: ignore
    
    #WE CAN CHOOSE SOME OPTION WITH THE SELECTOR---------------------------------
    options = ['1.) Register Name.', '2.) Register Codes.','3.) Show List.', 'Exit.']
    selection = 0 #the selector acts as a position in the list, position=0
    
    while True:
        #WE CAN CLEAR AND UPDATE THE SCREEN------------------------------------------
        screen.clear()
        screen.refresh()
        screen.addstr(0, 0, 'My Program - Main Menú', curses.A_BOLD)# type: ignore
        
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
        elif key == 10: # if the user presses enter then...
            if selection == len(options)-1:#if the selected option is the last then...
                break
            elif selection == 0:
                function1(my_dictionary, screen)  # we can call the function
                screen.addstr(len(options)+10, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            elif selection == 1:
                function2(my_dictionary, screen)
                screen.addstr(len(options)+10, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            elif selection == 2:
                function3(my_dictionary, screen)
                screen.addstr(len(options)+10, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()

curses.wrapper(show_menu)# type: ignore