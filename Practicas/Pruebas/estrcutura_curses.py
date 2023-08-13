import curses

def function1(my_dictionary,screen):
    pass

def function2(my_dictionary,screen):
    pass

def function3(my_dictionary,screen):
    pass

def show_menu(screen):
    #CREATE A DICTIONARY---------------------------------------------------------
    my_dictionary = {}#if a dictionary is used, this is the best time to call it
    
    #WE CAN CHOOSE THE COLORS----------------------------------------------------
    curses.start_color()# type: ignore
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)# type: ignore
    
    #WE CAN CHOOSE SOME OPTION WITH THE SELECTOR---------------------------------
    options = ['Option 1.', 'Option 2.','Option 3.', 'Salir.']
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
        elif key == 10: # si el usuario presiona Enter entonces...
            if selection == len(options)-1:#si es la ultima opcion
                break
            elif selection == 0:
                function1(my_dictionary, screen)  # Llamar a la función para agregar un estudiante
                screen.addstr(len(options)+10, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            elif selection == 1:
                function2(my_dictionary, screen)
                screen.addstr(len(options)+10, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            elif selection == 2:
                function3(my_dictionary, screen)

curses.wrapper(show_menu)# type: ignore