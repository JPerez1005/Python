'''Elabore un programa Python para gestionar el CRUD del archivo de datos PetShopping.json con las siguientes funcionalidades:

    a
Mostrar en pantalla todas las mascotas a la venta visualizando: Tipo, Raza, Precio y Servicios

    
Crear Nueva mascota con la posibilidad de múltiples ítems de Servicio

    
Mostrar los datos de Mascotas por Tipo elegido visualizando: Raza, Precio y Servicios

    
Actualizar los datos de una mascota consultada por índice (Mostrar el listado total y elegir por     índice)

    
Eliminar una mascota de la tienda (Mostrar el listado total y elegir por índice)'''

import curses
import json


def load_data():
    try:
        with open("PetShopping.json", "r") as file:
            my_dictionary = json.load(file)
    except FileNotFoundError:
        my_dictionary = {}
        my_dictionary['pets']=[]
    return my_dictionary

def integer_validation(entrance, screen, f1, c1):
    curses.echo()# type: ignore | see on screen what is being typed
    while True:
        input_str = screen.getstr(f1, 0, 10).decode(encoding="utf-8")
        if input_str.isdigit():#si realmente es un numero
            entrance = input_str#se remplazan los valores
            screen.addstr(0, c1, " " * 46)  # Borra la línea
            curses.noecho()# type: ignore | stop seeing on the screen what is being typed
            return entrance
        else:
            screen.addstr(f1, c1, " " * 10)  # Borra la línea
            screen.addstr(0, c1, "INGRESE SOLO NÚMEROS. Inténtelo nuevamente.!!!")#atencion
            screen.refresh()# se hace un refresh actuando como continue

def string_validation(entrance, screen, f1, c1):
    curses.echo()# type: ignore | see on screen what is being typed
    while True:
        input_str = screen.getstr(f1, c1, 100).decode(encoding="utf-8")
        if input_str.replace(" ", "").isalpha():#remplaza los espacios y a la vez verifica si son letras
            entrance = input_str#se remplazan los valores
            screen.addstr(0, c1, " " * 45)  # Borra la línea
            return entrance
        else:
            screen.addstr(f1, c1, " " * 100)  # Borra la línea
            screen.addstr(0, c1, "INGRESE SOLO LETRAS. Inténtelo nuevamente.!!!")#atencion
            screen.refresh()# we do a refresh acting like a continue
    curses.noecho()# type: ignore | stop seeing on the screen what is being typed

def add_pet(my_dictionary, screen):
    screen.clear()
    screen.refresh()
    
    screen.addstr(1, 0, "Ingrese el tipo de mascota: ")
    tipo = string_validation("", screen, 2, 0)
    
    screen.addstr(3, 0, "Ingrese la raza de la mascota: ")
    raza = string_validation("", screen, 4, 0)
    
    screen.addstr(5, 0, "Ingrese la talla de la mascota: (1.pequeño) (2.mediano) (3.grande)")
    talla = int(integer_validation("", screen, 6, 0))
    if talla==1:
        talla='pequeño'
    elif talla==2:
        talla='mediano'
    elif talla==3:
        talla='grande'
    else:
        screen.addstr(0, 0, "Opción inexistente...")
    
    screen.addstr(7, 0, "Ingrese el precio de la mascota: ")
    precio = int(integer_validation("", screen, 8, 0))
    
    servicios = []  # Lista para almacenar servicios
    while True:
        curses.echo()#type:ignore
        screen.addstr(9, 0, "Ingrese un servicio (o deje en blanco para terminar): ")
        servicio = screen.getstr(10, 0, 100).decode(encoding="utf-8").strip()
        
        if servicio.isdigit():
            screen.addstr(10, 0, " "*100)
            screen.addstr(0, 0, "No digite numeros")
            screen.refresh()
        elif servicio:
            screen.addstr(10, 0, " "*100)
            screen.addstr(0, 0, " "*18)
            servicios.append(servicio)
        else:
            break
        curses.noecho()#type:ignore
    
    my_dictionary['pets'].append({
        'tipo': tipo,
        'raza': raza,
        'talla': talla,
        'precio': precio,
        'servicios': servicios
    })
    
    with open('PetShopping.json', 'w') as archivo:
        json.dump(my_dictionary, archivo, indent=4)
    
    screen.addstr(0, 0, "Mascota agregada correctamente")
    screen.refresh()

def all_pets(my_dictionary, screen):
    screen.clear()
    screen.refresh()
    if not my_dictionary['pets']:
        screen.addstr(2, 0, "No hay mascotas registradas.")
    else:
        screen.addstr(1, 8, "+" + "-" * 54 + "+")
        screen.addstr(2, 8, "|{:^10}|{:^10}|{:^10}|{:^21}|".format("TIPO", "RAZA", "TALLA", "PRECIO"))
        screen.addstr(3, 8, "+" + "-" * 54 + "+")
        i = 4
        for pet in my_dictionary['pets']:
            screen.addstr(i, 8, "|{:<10}|{:<10}|{:<10}|{:<21}|".format(pet['tipo'], pet['raza'], pet['talla'], pet['precio']))
            i += 1

            # Muestra los servicios debajo de la información de la mascota
            services = ", ".join(pet['servicios'])
            screen.addstr(i, 8, "|{:<10}|{:<43}|".format("SERVICIOS", services))
            i += 1

            screen.addstr(i, 8, "+" + "-" * 54 + "+")
            i += 1
        screen.refresh()

def show_for_types(my_dictionary, screen):
    screen.clear()
    screen.refresh()
    
    if not my_dictionary['pets']:
        screen.addstr(2, 0, "No hay mascotas registradas.")
        screen.refresh()
        screen.getch()
        return
    
    # Obtener la lista de tipos de mascotas únicos
    tipos_mascotas = set(pet['tipo'] for pet in my_dictionary['pets'])
    
    screen.addstr(1, 0, "Tipos de mascotas disponibles:")
    
    for i, tipo in enumerate(tipos_mascotas, start=2):
        screen.addstr(i, 0, f"{i-1}. {tipo}")
    
    screen.addstr(len(tipos_mascotas)+2, 0, "Elija un tipo de mascota: ")
    seleccion = integer_validation("", screen, len(tipos_mascotas)+3, 0)
    seleccion = int(seleccion)  # Convertir la entrada a un entero
    
    if 1 <= seleccion <= len(tipos_mascotas):
        tipo_seleccionado = list(tipos_mascotas)[seleccion - 1]
        
        screen.addstr(0, 0, "Mascotas del tipo seleccionado:")
        i = 2
        
        for pet in my_dictionary['pets']:
            if pet['tipo'] == tipo_seleccionado:
                screen.addstr(i, 0, f"Tipo: {pet['tipo']}, Raza: {pet['raza']}, Precio: {pet['precio']}")
                i += 1
                servicios = ', '.join(pet['servicios'])
                screen.addstr(i, 0, f"Servicios: {servicios}")
                i += 1
                screen.addstr(i, 0, "-" * 40)
                i += 1
        
        screen.refresh()
        screen.getch()

def type(screen):
    screen.clear()
    screen.refresh()
    screen.addstr(1, 0, "Ingrese el tipo de mascota: ")
    tipo = string_validation("", screen, 2, 0)
    return tipo

def race(screen):
    screen.clear()
    screen.refresh()
    screen.addstr(3, 0, "Ingrese la raza de la mascota: ")
    raza = string_validation("", screen, 4, 0)
    return raza

def size(screen):
    screen.clear()
    screen.refresh()
    screen.addstr(5, 0, "Ingrese la talla de la mascota: (1.pequeño) (2.mediano) (3.grande)")
    talla = int(integer_validation("", screen, 6, 0))
    if talla==1:
        talla='pequeño'
    elif talla==2:
        talla='mediano'
    elif talla==3:
        talla='grande'
    else:
        screen.addstr(0, 0, "Opción inexistente...")
    return size

def price(screen):
    screen.clear()
    screen.refresh()
    screen.addstr(7, 0, "Ingrese el precio de la mascota: ")
    precio = int(integer_validation("", screen, 8, 0))
    return precio

def Services(screen):
    screen.clear()
    screen.refresh()
    pass

def modify_pet(my_dictionary, screen):
    screen.clear()
    screen.refresh()
    if not my_dictionary['pets']:
        screen.addstr(2, 0, "No hay mascotas registradas para modificar.")
        screen.getch()
        return
    
    screen.addstr(1, 0, "Ingrese el índice de la mascota a modificar: ")
    indice = integer_validation("", screen, 2, 0)
    indice = int(indice)
    
    if 0 <= indice < len(my_dictionary['pets']):
        pet = my_dictionary['pets'][indice]
        
        
        curses.start_color()# type: ignore
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)# type: ignore
        
        #WE CAN CHOOSE SOME OPTION WITH THE SELECTOR---------------------------------
        options = ['1.) change type.', '2.) change race.','3.) change size.','4.) change price.','5.) change services', 'Exit.']
        selection = 0 #the selector acts as a position in the list, position=0
        
        while True:
            #WE CAN CLEAR AND UPDATE THE SCREEN------------------------------------------
            screen.clear()
            screen.refresh()
            screen.addstr(0, 0, 'My Program - Menú', curses.A_BOLD)# type: ignore
            screen.addstr(3, 4, "+" + "-" * 54 + "+")
            screen.addstr(4, 4, "|{:^10}|{:^10}|{:^10}|{:^21}|".format("TIPO", "RAZA", "TALLA", "PRECIO"))
            screen.addstr(5, 4, "+" + "-" * 54 + "+")
            screen.addstr(6, 4, "|{:<10}|{:<10}|{:<10}|{:<21}|".format(pet['tipo'], pet['raza'], pet['talla'], pet['precio']))
            services = ", ".join(pet['servicios'])
            screen.addstr(7, 4, "|{:<10}|{:<43}|".format("SERVICIOS", services))
            screen.addstr(8, 4, "+" + "-" * 54 + "+")
            
            
            for i, option in enumerate(options):
                if i == selection:
                    screen.addstr(i+12, 5, option, curses.color_pair(1))# type: ignore
                else:
                    screen.addstr(i+12, 5, option)
            
            key = screen.getch()
            
            if key == curses.KEY_UP and selection > 0:# type: ignore
                selection -= 1
            elif key == curses.KEY_DOWN and selection < len(options)-1:# type: ignore
                selection += 1
            elif key == 10: # if the user presses enter then...
                if selection == len(options)-1:#if the selected option is the last then...
                    break
                elif selection == 0:
                    tipo=type(screen)  # we can call the function
                    my_dictionary['pets'][indice]['tipo']=tipo
                    with open('PetShopping.json', 'w') as archivo:
                        json.dump(my_dictionary, archivo, indent=4)
                    screen.getch()
                elif selection == 1:
                    raza=race(screen)
                    my_dictionary['pets'][indice]['raza']=raza
                    with open('PetShopping.json', 'w') as archivo:
                        json.dump(my_dictionary, archivo, indent=4)
                    screen.getch()
                elif selection == 2:
                    talla=size(screen)
                    my_dictionary['pets'][indice]['talla']=talla
                    with open('PetShopping.json', 'w') as archivo:
                        json.dump(my_dictionary, archivo, indent=4)
                    screen.getch()
                elif selection == 3:
                    precio=price(screen)
                    my_dictionary['pets'][indice]['precio']=precio
                    with open('PetShopping.json', 'w') as archivo:
                        json.dump(my_dictionary, archivo, indent=4)
                    screen.getch()
                elif selection == 4:
                    Services(screen)
                    screen.getch()
        
        with open('PetShopping.json', 'w') as archivo:
            json.dump(my_dictionary, archivo, indent=4)
        
        screen.addstr(len(my_dictionary['pets']) + 10, 0, "Mascota modificada correctamente.")
    else:
        screen.addstr(2, 0, "Índice inválido. Inténtelo nuevamente.")
    
    screen.getch()

def delete_pet(my_dictionary, screen):
    screen.clear()
    screen.refresh()
    if not my_dictionary['pets']:
        screen.addstr(2, 0, "No hay mascotas registradas para eliminar.")
        screen.getch()
        return
    while True:
        screen.addstr(1, 0, "Ingrese el índice de la mascota a eliminar: ")
        indice = integer_validation("", screen, 2, 0)
        indice = int(indice)
        
        if 0 <= indice < len(my_dictionary['pets']):
            pet = my_dictionary['pets'][indice]
            
            # Aquí puedes mostrar los detalles de la mascota antes de confirmar la eliminación
            screen.addstr(4, 0, f"¿Está seguro que desea eliminar la siguiente mascota?")
            screen.addstr(5, 0, f"Tipo: {pet['tipo']}, Raza: {pet['raza']}, Precio: {pet['precio']}")
            screen.addstr(6, 0, "Presione 'S' para confirmar la eliminación o cualquier otra tecla para cancelar.")
            screen.refresh()
            
            key = screen.getch()
            if key == ord('S') or key == ord('s'):
                # Aquí puedes implementar la lógica para eliminar la mascota del diccionario
                del my_dictionary['pets'][indice]
                
                with open('PetShopping.json', 'w') as archivo:
                    json.dump(my_dictionary, archivo, indent=4)
                screen.clear()
                screen.addstr(len(my_dictionary['pets']) + 5, 0, "Mascota eliminada correctamente.")
            else:
                screen.clear()
                screen.addstr(8, 0, "Eliminación cancelada.")
        else:
            screen.addstr(0, 0, "Índice inválido. Inténtelo nuevamente.")
            screen.refresh()
    
    screen.getch()

def show_menu(screen):
    my_dictionary=load_data()
    #CREATE A DICTIONARY---------------------------------------------------------
    #if a dictionary is used, this is the best time to call it
    
    #WE CAN CHOOSE THE COLORS----------------------------------------------------
    curses.start_color()# type: ignore
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)# type: ignore
    
    #WE CAN CHOOSE SOME OPTION WITH THE SELECTOR---------------------------------
    options = ['1.) add pet.', '2.) Show Pets.','3.) Show for types.','4.) Modify Pet.','5.) Delete Pet.', 'Exit.']
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
                add_pet(my_dictionary,screen)  # we can call the function
                #screen.addstr(len(options)+10, 0, "Presiona Enter para continuar...")# type: ignore
                screen.getch()
            elif selection == 1:
                all_pets(my_dictionary,screen)
                #screen.addstr(20, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            elif selection == 2:
                show_for_types(my_dictionary,screen)
                #screen.addstr(len(options)+10, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            elif selection == 3:
                modify_pet(my_dictionary,screen)
                #screen.addstr(len(options)+10, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            elif selection == 4:
                delete_pet(my_dictionary,screen)
                #screen.addstr(len(options)+10, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()

curses.wrapper(show_menu)# type: ignore