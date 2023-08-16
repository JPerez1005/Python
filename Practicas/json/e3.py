import json
def cargar_clientes():
    clientes = {}
    clientes['vendedores']=[]
    try:#Usamos un bloque try-except para manejar el caso en que el archivo no exista
        with open("ventas_de_la_compania.txt", "r") as archivo:#abrimos el archivo en modo lectura
            lineas = archivo.readlines()#leemos todas las lineas y la almacenamos en lineas
            for linea in lineas[1:]:#para cada linea desde la linea 2 hacia delante
                datos = linea.strip().split(",")#se quitan los espacios y se hace una lista
                clientes['vendedores'].append({
                    'Apellido':datos[0],
                    'Id':datos[1],
                    'ventas':[datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8]]
                })
                with open('ventas_de_la_compania.json', 'w') as archivo:
                    json.dump(clientes, archivo, indent=4)
    except FileNotFoundError:#(es la primera vez que se ejecuta el programa o el archivo no está presente).
        pass
    return clientes
cargar_clientes()
#hola