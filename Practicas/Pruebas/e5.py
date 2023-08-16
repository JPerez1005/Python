import json
import curses

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

def load_data():
    try:
        with open("PetShopping.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def save_data(data):
    with open("PetShopping.json", "w") as file:
        json.dump(data, file, indent=4)

def show_pets(screen, data):
    screen.clear()
    screen.refresh()
    screen.addstr(0, 0, "Lista de Mascotas a la Venta", curses.A_BOLD)#type:ignore
    
    for i, pet in enumerate(data):
        screen.addstr(i+2, 0, f"Tipo: {pet[i]['tipo']}, Raza: {pet[i]['raza']}, Precio: {pet[i]['precio']}")
        services = ", ".join(pet['servicios'])
        screen.addstr(i+2, 50, f"Servicios: {services}")

    screen.addstr(len(data)+3, 0, "Presiona Enter para continuar...")
    screen.getch()

def create_pet(screen, data):
    screen.clear()
    screen.refresh()
    screen.addstr(0, 0, "Crear Nueva Mascota", curses.A_BOLD)#type:ignore
    
    pet = {}
    pet['tipo'] = string_validation("Tipo de mascota: ", screen, 2, 0)
    pet['raza'] = string_validation("Raza: ", screen, 3, 0)
    pet['precio'] = integer_validation("Precio: ", screen, 4, 0)
    pet['servicios'] = []
    while True:
        curses.echo()# type: ignore
        service = string_validation("Servicio (Enter para terminar): ", screen, 5, 0)
        if service == "salir":
            break
        pet['servicios'].append(service)
        curses.noecho()#type:ignore
    
    data.append(pet)
    save_data(data)
    screen.addstr(len(data)+6, 0, "Mascota creada exitosamente. Presiona Enter para continuar...")
    screen.getch()

def filter_pets_by_type(screen, data):
    screen.clear()
    screen.refresh()
    screen.addstr(0, 0, "Filtrar por Tipo de Mascota", curses.A_BOLD)#type:ignore
    
    pet_type = string_validation("Ingrese el tipo de mascota a filtrar: ", screen, 2, 0)
    
    filtered_pets = [pet for pet in data if pet['tipo'].lower() == pet_type.lower()]
    if filtered_pets:
        show_pets(screen, filtered_pets)
    else:
        screen.addstr(3, 0, "No se encontraron mascotas con ese tipo.")
    
    screen.addstr(len(data)+4, 0, "Presiona Enter para continuar...")
    screen.getch()

def update_pet(screen, data):
    screen.clear()
    screen.refresh()
    screen.addstr(0, 0, "Actualizar Mascota", curses.A_BOLD)#type:ignore
    
    show_pets(screen, data)
    index = integer_validation("Ingrese el índice de la mascota a actualizar: ", screen, len(data)+2, 0)
    if 0 <= index < len(data):
        pet = data[index]
        screen.addstr(len(data)+3, 0, f"Mascota seleccionada: {pet['tipo']} - {pet['raza']}")
        pet['tipo'] = string_validation("Nuevo tipo de mascota: ", screen, len(data)+4, 0)
        pet['raza'] = string_validation("Nueva raza: ", screen, len(data)+5, 0)
        pet['precio'] = integer_validation("Nuevo precio: ", screen, len(data)+6, 0)
        pet['servicios'] = []
        while True:
            service = string_validation("Nuevo servicio (Enter para terminar): ", screen, len(data)+7, 0)
            if service == "":
                break
            pet['servicios'].append(service)
        save_data(data)
        screen.addstr(len(data)+8, 0, "Mascota actualizada exitosamente. Presiona Enter para continuar...")
    else:
        screen.addstr(len(data)+3, 0, "Índice de mascota inválido.")
    
    screen.getch()

def delete_pet(screen, data):
    screen.clear()
    screen.refresh()
    screen.addstr(0, 0, "Eliminar Mascota", curses.A_BOLD)#type:ignore
    
    show_pets(screen, data)
    index = integer_validation("Ingrese el índice de la mascota a eliminar: ", screen, len(data)+2, 0)
    if 0 <= index < len(data):
        pet = data.pop(index)
        save_data(data)
        screen.addstr(len(data)+3, 0, f"Mascota eliminada: {pet['tipo']} - {pet['raza']}. Presiona Enter para continuar...")
    else:
        screen.addstr(len(data)+3, 0, "Índice de mascota inválido.")
    
    screen.getch()



def main_menu(screen):
    data=load_data()
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
                create_pet(screen, data)  # we can call the function
                #screen.addstr(len(options)+10, 0, "Presiona Enter para continuar...")# type: ignore
                screen.getch()
            elif selection == 1:
                show_pets(screen, data)
                #screen.addstr(20, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            elif selection == 2:
                filter_pets_by_type(screen, data)
                screen.addstr(len(options)+10, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            elif selection == 3:
                update_pet(screen, data)
                screen.addstr(len(options)+10, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()
            elif selection == 4:
                delete_pet(screen, data)
                screen.addstr(len(options)+10, 0, "Presiona Enter para continuar...", curses.color_pair(2))# type: ignore
                screen.getch()

curses.wrapper(main_menu)#type:ignore
