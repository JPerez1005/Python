import json

# Función para abrir el archivo de datos
def abrir_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = json.load(archivo)
    except FileNotFoundError:
        contenido = []
    return contenido

# Función para guardar el archivo de datos
def guardar_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(contenido, archivo)

# Función para ingresar un nuevo cliente
def ingresar_cliente():
    id_cliente = input('ID del cliente: ')
    nombre = input('Nombre del cliente: ')
    edad = input('Edad del cliente: ')

    cliente = {
        'id': id_cliente,
        'nombre': nombre,
        'edad': edad,
        'compras': []
    }
    clientes.append(cliente)
    print('Cliente agregado correctamente.')

# Función para ingresar un nuevo producto
def ingresar_producto():
    codigo = input('Código del producto: ')
    valor_unitario = float(input('Valor unitario del producto: '))
    cantidad = int(input('Cantidad comprada: '))
    tipo_iva = int(input('Tipo de IVA (1: Exento, 2: Bienes, 3: General): '))

    producto = {
        'codigo': codigo,
        'valor_unitario': valor_unitario,
        'cantidad': cantidad,
        'tipo_iva': tipo_iva
    }
    productos.append(producto)
    print('Producto agregado correctamente.')

# Función para realizar la venta y generar la tirilla de pago
def realizar_venta():
    print('--- Realizar Venta ---')
    id_cliente = input('ID del cliente: ')

    cliente = next((c for c in clientes if c['id'] == id_cliente), None)
    if cliente is None:
        print('Cliente no encontrado. Venta cancelada.')
        return

    subtotal = 0
    total_iva = 0
    productos_vendidos = []

    print('Ingrese los productos vendidos:')
    while True:
        codigo = input('Código del producto (o "fin" para terminar): ')
        if codigo.lower() == 'fin':
            break

        # Buscar el producto por su código
        producto = next((p for p in productos if p['codigo'] == codigo), None)
        if producto is None:
            print('Producto no encontrado. Venta cancelada.')
            return

        cantidad = int(input('Cantidad vendida: '))

        valor_producto = producto['valor_unitario'] * cantidad
        valor_iva = valor_producto * (producto['tipo_iva'] / 100)
        valor_total = valor_producto + valor_iva

        subtotal += valor_producto
        total_iva += valor_iva

        producto_vendido = {
            'codigo': producto['codigo'],
            'valor_unitario': producto['valor_unitario'],
            'cantidad': cantidad,
            'valor_producto': valor_producto,
            'valor_iva': valor_iva,
            'valor_total': valor_total
        }
        productos_vendidos.append(producto_vendido)

        print('--- Tirilla de Pago ---')
        print('Producto:', producto['codigo'])
        print('Cantidad:', cantidad)
        print('Valor producto: $', valor_producto)
        print('Valor IVA: $', valor_iva)
        print('Valor total: $', valor_total)

    # Actualizar la información de compra del cliente
    cliente['compras'].extend(productos_vendidos)

    print('--- Total de la Compra ---')
    print('Subtotal: $', subtotal)
    print('Total IVA: $', total_iva)
    print('Total a Pagar: $', subtotal + total_iva)

# Función para mostrar las estadísticas de ventas
def mostrar_estadisticas():
    print('--- Estadísticas de Ventas ---')
    print('Total de productos vendidos:', len(productos))
    subtotal_sin_iva = sum(p['valor_unitario'] * p['cantidad'] for p in productos)
    total_iva = sum((p['valor_unitario'] * p['cantidad']) * (p['tipo_iva'] / 100) for p in productos)
    print('Valor total sin IVA: $', subtotal_sin_iva)
    print('Valor total de IVA: $', total_iva)
    print('Valor total con IVA: $', subtotal_sin_iva + total_iva)

# Nombre del archivo para almacenar los datos
nombre_archivo_productos = 'productos.json'
nombre_archivo_clientes = 'clientes.json'

# Abrir el archivo y cargar los productos existentes
productos = abrir_archivo(nombre_archivo_productos)

# Abrir el archivo y cargar los clientes existentes
clientes = abrir_archivo(nombre_archivo_clientes)

# Menú principal del programa
while True:
    print('--- PV micro-Acme ---')
    print('1. Ingresar Cliente')
    print('2. Ingresar Producto')
    print('3. Realizar Venta')
    print('4. Mostrar Estadísticas')
    print('5. Salir')

    opcion = input('Seleccione una opción: ')
    if opcion == '1':
        ingresar_cliente()
    elif opcion == '2':
        ingresar_producto()
    elif opcion == '3':
        realizar_venta()
    elif opcion == '4':
        mostrar_estadisticas()
    elif opcion == '5':
        # Guardar los productos y clientes en los archivos antes de salir
        guardar_archivo(nombre_archivo_productos, productos)
        guardar_archivo(nombre_archivo_clientes, clientes)
        break
    else:
        print('Opción inválida. Por favor, seleccione nuevamente.')

print('¡Hasta luego!')
