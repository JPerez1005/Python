import json
from datetime import date

Dia = date.today()

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

# Nombre del archivo para almacenar los datos
ArchivoProductos = 'productos.json'
ArchivoClientes = 'clientes.json'
ArchivoDia = f'{Dia}.json'
# Abrir el archivo y cargar los productos existentes
productos = CargarDatos(ArchivoProductos)

# Abrir el archivo y cargar los clientes existentes
clientes = CargarDatos(ArchivoClientes)

# Abrir compras de los clientes del día
dia= CargarDatos(ArchivoDia)

'''def Traspaso():
    try:
        # Abrir el archivo de origen en modo lectura
        with open(ArchivoClientes, "r") as archivo_origen:
            # Cargar los datos del archivo
            datos_origen = json.load(archivo_origen)
        for cliente in datos_origen.values():
            cliente['compras'] = []
        with open(ArchivoDia, "w") as archivo_destino:
            json.dump(datos_origen, archivo_destino)
    except FileNotFoundError:
        contenido = []
    return contenido'''

def AgregarCliente():
    print('-'*5,'Este es el registro de clientes','-'*5)
    id_cliente = input('ID del cliente: ')
    nombre = input('Nombre del cliente: ')
    edad = input('Edad del cliente: ')

    cliente = {
        'id': id_cliente,
        'nombre': nombre,
        'edad': edad,
        'compras':[]
    }
    clientes.append(cliente)
    dia.append(cliente)
    print('Cliente agregado correctamente.')

def IngresarProducto():
    codigo = input('Código del producto: ')
    nombre=input('Nombre del Producto: ')
    valor_unitario = float(input('Valor unitario del producto: '))
    cantidad = int(input('Cantidad de productos: '))
    tipo_iva = int(input('Tipo de IVA (1: Exento, 2: Bienes, 3: General): '))

    producto = {
        'codigo': codigo,
        'nombre':nombre,
        'valor_unitario': valor_unitario,
        'cantidad': cantidad,
        'tipo_iva': tipo_iva,
        'Fecha de Ingreso':Dia
    }
    productos.append(producto)
    print('Producto agregado correctamente.')

def RealizarVenta():
    print('--- Realizar Venta ---')
    id_cliente = input('ID del cliente: ')#el usuario coloca el id,

    cliente = next((c for c in clientes if c['id'] == id_cliente), None)
    if cliente is None:#si no existe el id entonces...
        print('Cliente no encontrado. Venta cancelada.')
        print('Agregaremos el cliente...')
        AgregarCliente()#agregamos el cliente si es que no existe
        RealizarVenta()
        return
    '''Traspaso()'''
    clientedia = next((c for c in dia if c['id'] == id_cliente), None)
    subtotal = 0
    total_iva = 0
    productos_vendidos = []

    print('Ingrese los productos vendidos:')
    while True:
        codigo = input('Código del producto (o "fin" para terminar): ')
        if codigo.lower().strip() == 'fin':#si el usuario digita fin se sale
            break

        # Buscar el producto por su código
        producto = next((p for p in productos if p['codigo'] == codigo), None)
        if producto is None:#si el producto no existe entonces...
            print('Producto no encontrado. Venta cancelada.')
            return

        cantidad = int(input('Cantidad de productos a vender: '))
        #cantidad de productos que el usuario comprará

        if cantidad>producto['cantidad']:
            print('Esa cantidad de productos es mas de los que hay')
            print(f'tenemos {producto["cantidad"]} {producto["nombre"]}')
            continue
        
        #ahora restamos la cantidad de productos
        producto['cantidad']=producto['cantidad']-cantidad
        #buscamos el valor del producto y lo multiplicamos por la cantidad
        valor_producto = producto['valor_unitario'] * cantidad
        #buscamos cuanto iva tiene y lo multiplicamos por el producto
        valor_iva = valor_producto * (producto['tipo_iva'] / 100)
        #sumamos el iva y el producto para obtener el valor total
        valor_total = valor_producto + valor_iva

        #siendo subtotal el valor de todos los productos sin el iva
        subtotal += valor_producto
        #siendo total iva el total de ivas de la suma de todos los productos
        total_iva += valor_iva

        #colocamos todos los valores en el diccionario
        producto_vendido = {
            'codigo': producto['codigo'],
            'nombre': producto['nombre'],
            'valor_unitario': producto['valor_unitario'],
            'cantidad': cantidad,
            'valor_producto': valor_producto,
            'valor_iva': valor_iva,
            'valor_total': valor_total,
            'Fecha de compra': Dia
        }
        
        #enlistamos todos los productos al final
        productos_vendidos.append(producto_vendido)
        
        #mostramos la informacion
        print('--- Tirilla de Pago ---')
        print('Producto:', producto['codigo'])
        print('Cantidad:', cantidad)
        print('Valor producto: $', valor_producto)
        print('Valor IVA: $', valor_iva)
        print('Valor total: $', valor_total)

    # Actualizar la información de compra del cliente
    #Es decir las compras vacias del cliente registrado las llenamos
    #si es que ese fue el cliente que compró el producto
    cliente['compras'].extend(productos_vendidos)

    #por ultimo simplemente mostramos la información
    print('--- Total de la Compra ---')
    print('Subtotal: $', subtotal)
    print('Total IVA: $', total_iva)
    print('Total a Pagar: $', subtotal + total_iva)

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
        print('2. Ingresar Producto')
        print('3. Realizar Venta')
        print('4. Mostrar Estadísticas')
        print('5. Salir')

        opcion = input('Seleccione una opción: ')
        if opcion == '1':
            AgregarCliente()
        elif opcion == '2':
            IngresarProducto()
        elif opcion == '3':
            RealizarVenta()
        elif opcion == '4':
            MostrarEstadistica()
        elif opcion == '5':
            # Guardar los productos y clientes en los archivos antes de salir
            Actualizar(ArchivoProductos, productos)
            Actualizar(ArchivoClientes, clientes)
            Actualizar(ArchivoDia, dia)
            break
        else:
            print('Opción inválida. Por favor, seleccione nuevamente.')

    print('¡Hasta luego!')

menu()
