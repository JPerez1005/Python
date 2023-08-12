import curses

def show_menu(screen):
    #configuracion de la pantalla
    curses.curs_set(0)#ocultar el cursor
    screen.clear()
    
    #Definir opciones del menu
    options=['Option 1','Option 2','Option 3','Salir']
    selection=0
    
    while True:
        #mostrar el menu
        screen.clear()
        for i, option in enumerate(options):
            if i==selection:
                screen.addstr(i+1,0,option,curses.A_REVERSE)#resaltar la opcion seleccionada
            else:
                screen.addstr(i+1,0,option)
            #capturar la entrada del usuario
        key=screen.getch()
            
            #procesar la entrada del usuario
        if key==curses.KEY_UP and selection>0:
            selection-=1
        elif key==curses.KEY_DOWN and selection<len(options)-1:
            selection+=1
        elif key==10: #Enter
            if selection==len(options)-1:
                break
            else:
                screen.addstr(len(options),0,f'Has elegido {options[selection]}. Presiona Enter para continuar...')
                screen.getch()

curses.wrapper(show_menu)