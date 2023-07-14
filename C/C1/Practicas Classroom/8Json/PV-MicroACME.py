# Importar el módulo
import json
import os
MicroMercado = "Acme.json"
cont=0
def crear_archivo_json():
    if not os.path.exists(MicroMercado):# si el archivo ya existe entonces...
        empleados = {}  # Creamos el diccionario de empleados
        with open(MicroMercado, 'w') as archivo:
            json.dump(empleados, archivo)
        print("Archivo JSON creado exitosamente.")
    else:
        print("El archivo ya existe. No se creó uno nuevo.")

def verificar_archivo_vacio():
    with open(MicroMercado, 'r') as archivo:
        contenido = json.load(archivo)
        
        if contenido: # Verificar si el contenido del archivo no está vacío
            print("El archivo contiene datos.")
        else:
            print("El archivo está vacío.")

def AsignacionProductos():
    id=input('Digite el id del producto: ')
    nombre=input('Digite el nombre del producto: ')
    cant=input('Digite la cantidad de productos que hay: ')
    valor=input('Digite el valor de producto: ')
    TipoIva=input('Digite el tipo de iva: ')
    if TipoIva=='1':
        TipoIva=0
    elif TipoIva=='2':
        TipoIva=0.05
    elif TipoIva=='3':
        TipoIva=0.19
    
    with open(MicroMercado, "r") as archivo:
        contenido = json.load(archivo)
    productos = {
            'id':id,
            "producto": nombre,
            "cantidad": cant,
            "valor": valor,
            "Tipo de Iva": TipoIva
        }
    contenido[id] = productos
    with open('Acme.json','w') as archivo:
        json.dump(contenido, archivo)

def RegistroClientes(idP,name,old):
    with open(MicroMercado, "r") as archivo:
        contenido = json.load(archivo)
    clientes={
        'Cedula':idP,
        'Nombre':name,
        'Edad':old
    }
    contenido[idP] = clientes
    with open('Acme.json','w') as archivo:
        json.dump(contenido, archivo)

def RealizarCompra():
    while True:
        global cont
        cont = cont + 1
        
        with open(MicroMercado, "r") as archivo:
            contenido = json.load(archivo)
        
        if cont == 1:
            cedula = input('Digite número de cédula: ')
            nombre = input('Digite nombre: ')
            edad = input('Edad: ')
            RegistroClientes(cedula, nombre, edad)
            ValorTotal = 0
            productos_comprados = []
        
        codigo = input('Digite el código del producto: ')
        cant = input('Digite la cantidad de productos: ')
        
        with open(MicroMercado, "r") as archivo:
            contenido = json.load(archivo)
        
        if codigo in contenido:
            producto = contenido[codigo]
            convertido = int(producto['cantidad'])
            
            if convertido <= 0:
                print('No tenemos más de esos productos')
            else:
                rest = str(int(producto['cantidad']) - int(cant))
                print("Datos del producto:")
                print('Código:', codigo)
                print('Valor: {:,}'.format(int(producto['valor'])))
                print('Cantidad de productos restantes:', rest)
                print('Tipo de IVA:', producto['Tipo de Iva'])
                
                productos = {
                    'id': producto['id'],
                    'producto': producto['producto'],
                    'cantidad': rest,
                    'valor': producto['valor'],
                    'Tipo de Iva': producto['Tipo de Iva']
                }
                
                contenido[codigo] = productos
                
                with open('Acme.json','w') as archivo:
                    json.dump(contenido, archivo)
                
                codCompra = str(int(codigo) + 100)
                
                if producto['Tipo de Iva'] == 0:
                    print('Exento de IVA')
                    CompraArt = int(cant) * int(producto['valor'])
                elif producto['Tipo de Iva'] == 0.05:
                    print('Tiene un IVA del 5%')
                    CompraArt = float(cant) * float(producto['valor']) * 0.05
                elif producto['Tipo de Iva'] == 0.19:
                    print('Tiene un IVA del 19%')
                    CompraArt = float(cant) * float(producto['valor']) * 0.19
                
                ValorTotal = ValorTotal + int(CompraArt)
                
                producto_comprado = {
                    'Código del Producto': codigo,
                    'Valor del producto': producto['valor'],
                    'Cantidad comprada': cant,
                    'Tipo Iva': producto['Tipo de Iva']
                }
                
                productos_comprados.append(producto_comprado)
                
                compras = {
                    'Cedula Cliente': cedula,
                    'Nombre Cliente': nombre,
                    'Codigo de compra': codCompra,
                    'Productos': productos_comprados,
                    'Valor Total': str(ValorTotal),
                    'Numero de compra': cont
                }
                
                contenido[codCompra] = compras
                
                with open('Acme.json','w') as archivo:
                    json.dump(contenido, archivo)
                
                print('Compra realizada')
        else:
            print('El Producto no existe')
        
        d = input('Desea seguir? (s/n): ')
        
        if d.lower() == 'n':
            print('-'*5, f'Recibo de {nombre}', '-'*5, '\n')
            print('-'*5, f'Código de compra {codCompra}', '-'*5, '\n')
            print(f'Cédula: {cedula} \n')
            print(f'Nombre: {nombre} \n\n')
            
            for producto in productos_comprados:
                print('\n', '-'*5)
                print('Código:', producto['Código del Producto'])
                print('Valor:', producto['Valor del producto'])
                print('Cantidad comprada:', producto['Cantidad comprada'])
                print('Tipo IVA:', producto['Tipo Iva'])
            
            print(f'\n\nValor Total: {ValorTotal} \n')
            
            ValorTotal = 0
            cont = 0
            return

def ArticulosVendidos():
    with open(MicroMercado, "r") as archivo:
        contenido = json.load(archivo)

    cant = 0

    for key, value in contenido.items():
        if key.isdigit() and 'Productos' in value and len(value['Productos']) > 0:
            cant += int(value['Productos'][0]['Cantidad comprada'])

    print("La cantidad total de artículos vendidos es:", cant)


def menu():
    crear_archivo_json()
    verificar_archivo_vacio()
    while True:
        print("*** MicroMercado ACME ***")
        print("MENU")
        print("1- Gestionar Productos.")
        print("2- Gestionar Clientes.")
        print('3- Salir')
        opcion = input("Escoja una opción (1-3): ")
        print("--------------------")
        if opcion == "1":
            print("*** MicroMercado ACME ***")
            print("Gestión Productos")
            print("1- Ingresar Productos.")
            print('2- Realizar compra.')
            print('3- Ver cantidad de articulos vendidos.')
            opcion = input("Escoja una opción (1-3): ")
            print("--------------------")
            if opcion=='1':
                AsignacionProductos()
            elif opcion=='2':
                RealizarCompra()
            elif opcion=='3':
                ArticulosVendidos()
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
            print("--------------------")
        elif opcion=='2':
            print("*** MicroMercado ACME ***")
            print("Gestión Clientes")
        elif opcion=='3':
            confirmacion = input("¿Está seguro de que desea salir? (S/N): ")
            if confirmacion.upper() == "S":
                print("¡Hasta luego!")
                break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            print("--------------------")

menu()