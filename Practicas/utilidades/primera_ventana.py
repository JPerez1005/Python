import curses

def show_menu(screen):
    curses.start_color()#Iniciar el modo de color
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_CYAN)#Definir un par de colores
    
    screen.clear()
    screen.refresh()

    #crear ventana
    menu_win=curses.newwin(10,40,5,10)

    menu_win.box()
    menu_win.addstr(1,1,'Mi menú',curses.A_BOLD)
    menu_win.refresh()

curses.wrapper(show_menu)