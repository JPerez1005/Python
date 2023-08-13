import curses

def show_menu(screen):
    curses.start_color()# type: ignore #Iniciar el modo de color
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_CYAN)# type: ignore #Definir un par de colores
    
    screen.clear()
    screen.refresh()
    
    #Definir opciones del menu
    options=['Option 1','Option 2','Option 3','Salir']
    selection=0
    
    while True:
        screen.clear()
        screen.addstr(0,0,'Mi programa - Menú Principal', curses.A_BOLD)# type: ignore
        #Mostrar el menú con colores
        for i, option in enumerate(options):
            if i==selection:
                screen.addstr(i+2,5,option,curses.color_pair(1)) # type: ignore
            else:
                screen.addstr(i+2,5,option)
                #capturar la entrada del usuario
        key=screen.getch()
                
                #procesar la entrada del usuario
        if key==curses.KEY_UP and selection>0:# type: ignore
            selection-=1
        elif key==curses.KEY_DOWN and selection<len(options)-1:# type: ignore
            selection+=1
        elif key==10: #Enter
            if selection==len(options)-1:
                break
            else:
                screen.addstr(len(options)+2,0,f'Has elegido {options[selection]}. Presiona Enter para continuar...',curses.color_pair(2))# type: ignore
                screen.getch()

curses.wrapper(show_menu)# type: ignore