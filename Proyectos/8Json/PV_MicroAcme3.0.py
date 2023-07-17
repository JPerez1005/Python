import json
from datetime import date

Dia = date.today()

# Función personalizada para codificar objetos date a JSON
def date_encoder(obj):
    if isinstance(obj, date):
        return obj.isoformat()

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
        json.dump(contenido, archivo, default=date_encoder)

# Nombre del archivo para almacenar los datos
ArchivoProductos = 'productos.json'
ArchivoClientes = 'clientes.json'
ArchivoDia = f'{Dia}.json'
# Abrir el archivo y cargar los productos existentes
productos = CargarDatos(ArchivoProductos)

# Abrir el archivo y cargar los clientes existentes
clientes = CargarDatos(ArchivoClientes)

# Abrir compras de los clientes del día
dia = CargarDatos(ArchivoDia)

def AgregarCliente():
    print('-'*5,'Este es el registro de clientes','-'*5)
    id_cliente = input('ID del cliente: ')
    nombre = input('Nombre del cliente: ')
    edad = input('Edad del cliente: ')

    cliente = {
        'id': id_cliente,
        'nombre': nombre,
        'edad': edad
    }
    clientes.append(cliente)
    print('Cliente agregado correctamente.')

def ModificarCliente():
    print('-'*5,'Modificar Cliente','-'*5)
    id_cliente = input('ID del cliente a modificar: ')

    cliente = next((c for c in clientes if c['id'] == id_cliente), None)
    if cliente is None:
        print('Cliente no encontrado.')
        return

    print('Cliente encontrado. Datos actuales:')
    print('ID:', cliente['id'])
    print('Nombre:', cliente['nombre'])
    print('Edad:', cliente['edad'])

    nuevo_nombre = input('Nuevo nombre (dejar en blanco para mantener el actual): ')
    nuevo_edad = input('Nueva edad (dejar en blanco para mantener la actual): ')

    if nuevo_nombre:
        cliente['nombre'] = nuevo_nombre
    if nuevo_edad:
        cliente['edad'] = nuevo_edad

    print('Cliente modificado correctamente.')

def EliminarCliente():
    print('-'*5,'Eliminar Cliente','-'*5)
    id_cliente = input('ID del cliente a eliminar: ')

    cliente = next((c for c in clientes if c['id'] == id_cliente), None)
    if cliente is None:
        print('Cliente no encontrado.')
        return

    clientes.remove(cliente)
    print('Cliente eliminado correctamente.')

def IngresarProducto():
    codigo = input('Código del producto: ')
    nombre = input('Nombre del Producto: ')
    valor_unitario = float(input('Valor unitario del producto: '))
    cantidad = int(input('Cantidad de productos: '))
    tipo_iva = int(input('Tipo de IVA (1: Exento, 2: Bienes, 3: General): '))

    producto = {
        'codigo': codigo,
        'nombre': nombre,
        'valor_unitario': valor_unitario,
        'cantidad': cantidad,
        'tipo_iva': tipo_iva,
        'Fecha de Ingreso': Dia
    }
    productos.append(producto)
    print('Producto agregado correctamente.')

def ModificarProducto():
    print('-'*5,'Modificar Producto','-'*5)
    codigo_producto = input('Código del producto a modificar: ')

    producto = next((p for p in productos if p['codigo'] == codigo_producto), None)
    if producto is None:
        print('Producto no encontrado.')
        return

    print('Producto encontrado. Datos actuales:')
    print('Código:', producto['codigo'])
    print('Nombre:', producto['nombre'])
    print('Valor unitario:', producto['valor_unitario'])
    print('Cantidad:', producto['cantidad'])
    print('Tipo de IVA:', producto['tipo_iva'])

    nuevo_nombre = input('Nuevo nombre (dejar en blanco para mantener el actual): ')
    nuevo_valor_unitario = input('Nuevo valor unitario (dejar en blanco para mantener el actual): ')
    nueva_cantidad = input('Nueva cantidad (dejar en blanco para mantener la actual): ')
    nuevo_tipo_iva = input('Nuevo tipo de IVA (dejar en blanco para mantener el actual): ')

    if nuevo_nombre:
        producto['nombre'] = nuevo_nombre
    if nuevo_valor_unitario:
        producto['valor_unitario'] = float(nuevo_valor_unitario)
    if nueva_cantidad:
        producto['cantidad'] = int(nueva_cantidad)
    if nuevo_tipo_iva:
        producto['tipo_iva'] = int(nuevo_tipo_iva)

    print('Producto modificado correctamente.')

def EliminarProducto():
    print('-'*5,'Eliminar Producto','-'*5)
    codigo_producto = input('Código del producto a eliminar: ')

    producto = next((p for p in productos if p['codigo'] == codigo_producto), None)
    if producto is None:
        print('Producto no encontrado.')
        return

    productos.remove(producto)
    print('Producto eliminado correctamente.')

def RealizarVenta():
    print('--- Realizar Venta ---')
    id_cliente = input('Digite el id del cliente: ')

    cliente_completo = next((c for c in clientes if c['id'] == id_cliente), None)
    if cliente_completo is None:
        print('Cliente no encontrado. Venta cancelada.')
        print('Agregaremos el cliente...')
        AgregarCliente()
        RealizarVenta()
        return

    subtotal = 0
    total_iva = 0
    productos_vendidos = []

    print('Ingrese los productos vendidos:')
    while True:
        codigo = input('Código del producto (o "fin" para terminar): ')
        if codigo.lower().strip() == 'fin':
            break

        producto = next((p for p in productos if p['codigo'] == codigo), None)
        if producto is None:
            print('Producto no encontrado. Venta cancelada.')
            return

        cantidad = int(input('Cantidad de productos a vender: '))
        if cantidad > producto['cantidad']:
            print('Esa cantidad de productos es mayor a la disponible.')
            print(f'Tenemos {producto["cantidad"]} {producto["nombre"]} disponibles.')
            continue

        producto['cantidad'] -= cantidad

        valor_producto = producto['valor_unitario'] * cantidad
        valor_iva = valor_producto * (producto['tipo_iva'] / 100)
        valor_total = valor_producto + valor_iva

        subtotal += valor_producto
        total_iva += valor_iva

        producto_vendido = {
            'codigo': producto['codigo'],
            'nombre': producto['nombre'],
            'valor_unitario': producto['valor_unitario'],
            'cantidad': cantidad,
            'valor_producto': valor_producto,
            'valor_iva': valor_iva,
            'valor_total': valor_total,
            'cliente': cliente_completo
        }

        productos_vendidos.append(producto_vendido)

        print('--- Tirilla de Pago ---')
        print('Producto:', producto['codigo'])
        print('Cantidad:', cantidad)
        print('Valor producto: $', valor_producto)
        print('Valor IVA: $', valor_iva)
        print('Valor total: $', valor_total)

    print('--- Total de la Compra ---')
    print('Subtotal: $', subtotal)
    print('Total IVA: $', total_iva)
    print('Total a Pagar: $', subtotal + total_iva)

    dia.extend(productos_vendidos)

def MostrarEstadistica():
    print('--- Estadísticas de Ventas ---')
    print('Total de productos vendidos:', len(productos))
    subtotal_sin_iva = sum(p['valor_unitario'] * p['cantidad'] for p in productos)
    total_iva = sum((p['valor_unitario'] * p['cantidad']) * (p['tipo_iva'] / 100) for p in productos)
    print('Valor total sin IVA: $', subtotal_sin_iva)
    print('Valor total de IVA: $', total_iva)
    print('Valor total con IVA: $', subtotal_sin_iva + total_iva)

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
            AgregarCliente()
        elif opcion == '2':
            ModificarCliente()
        elif opcion == '3':
            EliminarCliente()
        elif opcion == '4':
            IngresarProducto()
        elif opcion == '5':
            ModificarProducto()
        elif opcion == '6':
            EliminarProducto()
        elif opcion == '7':
            RealizarVenta()
        elif opcion == '8':
            MostrarEstadistica()
        elif opcion == '9':
            # Guardar los productos y clientes en los archivos antes de salir
            Actualizar(ArchivoProductos, productos)
            Actualizar(ArchivoClientes, clientes)
            Actualizar(ArchivoDia, dia)
            break
        else:
            print('Opción inválida. Por favor, seleccione nuevamente.')

    print('¡Hasta luego!')

menu()
