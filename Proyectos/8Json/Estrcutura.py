import json

# Función para abrir el archivo de datos
def CargarDatos(NombreArchivo):
    try:
        with open(NombreArchivo, 'r') as archivo:
            contenido = json.load(archivo)
    except FileNotFoundError:
        contenido = []
    return contenido

# Función para guardar el archivo de datos
def Actualizar(NombreArchivo, contenido):
    with open(NombreArchivo, 'w') as archivo:
        json.dump(contenido, archivo)

Archivo='archivo.json'#creamos el archivo
# Abrir el archivo y cargar los datos existentes
contenido = CargarDatos(Archivo)
#en contenido se muestran los datos de ese archivo

# Menú principal del programa
def menu():
    while True:
        print('--- PV micro-Acme ---')
        print('1. Ingresar Cliente')
        print('2. Modificar Cliente')
        print('3. Eliminar Cliente')
        print('4. Ingresar Producto')
        print('5. Modificar Producto')
        print('6. Eliminar Producto')
        print('7. Realizar Venta')
        print('8. Mostrar Estadísticas')
        print('9. Salir')

        opcion = input('Seleccione una opción: ')
        if opcion == '1':
            print()
        elif opcion == '2':
            print()
        elif opcion == '3':
            print()
        elif opcion == '4':
            print()
        elif opcion == '5':
            print()
        elif opcion == '6':
            print()
        elif opcion == '7':
            print()
        elif opcion == '8':
            print()
        elif opcion == '9':
            # Guardar los productos y clientes en los archivos antes de salir
            Actualizar(Archivo, contenido)
            break
        else:
            print('Opción inválida. Por favor, seleccione nuevamente.')

    print('¡Hasta luego!')

menu()
