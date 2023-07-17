#MICROMERCADO ACME
# Punto de Venta para el Micromercado ACME con capacidad para gestionar productos y registrar ventas.
# Todos los productos quedan registrados en un Archivo y pueden ser modificados o eliminados según criterio de Gerencia
# Todas las ventas quedan registradas en un Archivo, unico para cada día. Ventas pueden ser moficadas o elimindas por si se cometen 
# errores humanos al momento de registrarlas o si se tiene algún problema con el cliente.
# Cada día el Sistema crea un nuevo Archivo en blanco para registrar todas las ventas diarias.
# El sistema cuenta con un apartado de Detalle donde se muestra en consola las ventas totales del Día detalladas.
# Si el sistema se cierra inesperadamente sin finalizar el día, se posee la capacidad de recuperar los datos hasta el breakpoint.
# El sistema debe ser lo más intuitivo para facilitar la labor al Cajero al momento de usarlo.

import json
from datetime import date
#Creación de Diccionarios para almacenar en Memoria
Sales = {}
Products = {}
#Fecha del Día para crear Archivo de ventas
Dia = date.today()
#Cargar Archivo de Ventas del día
try:
    SalesFile = open(f"{Dia}.json", "r")
    Sales = json.load(SalesFile)
    SalesFile.close()
except FileNotFoundError:
    SalesFile = open(f"{Dia}.json", "w")
    SalesFile.close()
#Cargar Archivo de Productos
try:
    with open("Products.json", "r") as file:
        products = json.load(file)
except FileNotFoundError:
    ProductsFile = open("Products.json", "w")
    ProductsFile.close()

#******************************** FUNCIONES VALIDACIÓN Y NOTIFICACIÓN ********************************
#Función Mensaje Error -> Se utiliza para imprimir diferentes Notificaciones durante el proceso.
def MsgNotify(msg):
    print("\n NOTIFY!", msg)
    input(" -> Presione cualquier letra para regresar al Menú")
    print("=" * 45)

#Función Validar Entero -> Los datos numericos que se requieren deben ser todos Positivos y mayores que 0
def LeerEntero(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 0:
                MsgNotify("Error! Dato no valido")
                continue
            return n
        except ValueError:
            print("Error! Ingrese un numero de codigo valido")


#Función Leer String -> Evita que se ingresen Nombres Vacios
def LeerString(msg):
    while True:
        try:
            Name = input(msg)
            Name = Name.strip()
            if Name == "":
                MsgNotify("Error! Ingrese un nombre no Vacio")
                continue
            return Name
        except Exception as e:
            print("Error al ingresar el nombre.", e.message)

#Función para Actualizar Archivo de Productos
def UpdateProducts(Dicc):
    with open("Products.json", "w") as ProductsFile:
        json.dump(Dicc, ProductsFile)

#Función para Actualizar Archivo de Ventas
def UpdateSales(Dicc):
    Dia = date.today()
    with open(f"{Dia}.json", "w") as ProductsFile:
        json.dump(Dicc, ProductsFile)
#********************************** FUNCION MENÚ PRINCIPAL ************************************
#Función Mostrar Menú Principal, con los submenús
def MainMenu():
    while True:
        print("\n","=" * 40)
        print("*** MICROMERCADO ACME *** ")
        print("      MENÚ PRINCIPAL")
        print("1-   Ventas")
        print("2-   Productos")
        print("3-   Detalle")
        print("4-   Cerrar Caja")
        try:
            Opc = int(input("\t>>Escoja una opción (1-4)? "))
            if Opc < 0 or Opc > 4:                                      #Solo valido opciones entre 1 y 4
                MsgNotify("Opción no valida")
                continue
            else:
                return Opc
        except ValueError:
            print("Error! Ingrese un numero entero valido")

#******************************* FUNCIONES APARTADO DE VENTAS ********************************


#Función para Registrar nueva venta a cliente
def NuevaVenta(Sales, Products):
    IDCliente = LeerString("Identificación del Cliente: ")
    if not IDCliente in Sales:
        Sales[IDCliente] = {}
    while True:
        Cod = LeerString("Producto Comprado (0 - Finalizar Compra): ")
        if Cod == "0":
            break
        if Cod in Products.keys():
            Sales[IDCliente][Cod] = {}
            Cant = LeerEntero("Cantidad Comprada: ")
            Sales[IDCliente][Cod]["Cant"] = Cant
        else:
            MsgNotify("PRODUCTO NO REGISTRADO")
            continue
    Sales = CalcularVenta(IDCliente, Sales, Products)
    TirillaPago(IDCliente, Sales, Products)
    UpdateSales(Sales)
    return Sales

#Función para Modificar venta registrada (Error Humano al ingresar dato)
def ModificarVenta(Sales, Products):
    IDCliente = LeerString("Identificación del Cliente: ")
    if IDCliente in Sales.keys():
        Cod = LeerString("Producto a Modificar: ")
        if Cod in Sales[IDCliente].keys():
            Cant = LeerEntero("Leer Cantidad: ")
            if Cant == 0:
                Sales[IDCliente].pop(str(Cod))
                MsgNotify("VENTA MODIFICADA EXITOSAMENTE")
                print(len(Sales[IDCliente].keys()))
                if len(Sales[IDCliente].keys()) == 1:
                    Sales.pop(IDCliente)
                    UpdateSales(Sales)
                return Sales
            Sales[IDCliente][Cod]["Cant"] = Cant
            MsgNotify("VENTA MODIFICADA EXITOSAMENTE")
            Sales = CalcularVenta(IDCliente, Sales, Products)
            TirillaPago(IDCliente, Sales, Products)
            return Sales
        else:
            MsgNotify("Producto no registrado en Factura")
    else:
        MsgNotify("VENTA NO REGISTRADA")
    return Sales

#Función para Eliminar venta registrada (Problemas con el cliente)
def EliminarVenta(Sales):
    IDCliente = LeerString("Identificación del Cliente: ")
    if IDCliente in Sales:
        Sales.pop(IDCliente)
        MsgNotify("VENTA ELIMINADA EXITOSAMENTE")
        UpdateSales(Sales)

#Función para Calcular valores de Venta
def CalcularVenta(Cliente, Sales, Products):
    TotalPagar = 0
    for Cod in Sales[Cliente].keys():
        if Cod == "TotalPagar":
            break
        Sales[Cliente][Cod]["VlrProd"] = Sales[Cliente][Cod]["Cant"] * Products[Cod]["VlrUni"]
        Sales[Cliente][Cod]["VlrIVA"] = Sales[Cliente][Cod]["VlrProd"] * Products[Cod]["IVA"]
        Sales[Cliente][Cod]["VlrTotal"] = Sales[Cliente][Cod]["VlrProd"] + Sales[Cliente][Cod]["VlrIVA"]
        TotalPagar += Sales[Cliente][Cod]["VlrTotal"]
    Sales[Cliente]["TotalPagar"] = TotalPagar
    UpdateSales(Sales)
    return Sales

#Función para Imprimir Tirilla de Pago
def TirillaPago(IDCliente, Sales, Products):
    print("*" * 14, "TIRILLA DE PAGO", "*" * 14)
    print(f"ID Cliente: {IDCliente}")
    print("|{:<6}|{:<15}|{:>6}|{:>15}|{:>15}|{:>15}|".format("COD", "PRODUCTO", "CANT", "VLR PRODUCTO", "VLR IVA", "VLR TOTAL"))
    for Cod in Sales[IDCliente].keys():
        if Cod == "TotalPagar":
            break
        print("|{:<6}|{:<15}|{:>6}|{:>15,}|{:>15,}|{:>15,}|".format(Cod, Products[Cod]["Name"], Sales[IDCliente][Cod]["Cant"], Sales[IDCliente][Cod]["VlrProd"], Sales[IDCliente][Cod]["VlrIVA"], Sales[IDCliente][Cod]["VlrTotal"]))
        print("+------+---------------+------+---------------+---------------+---------------+")
    print()
    print(f"TOTAL A PAGAR: ", Sales[IDCliente]["TotalPagar"])

#Función Mostrar SubMenú de Ventas
def SalesMenu(Sales, Products):
    while True:
        print("\n","=" * 40)
        print("*** SUBMENÚ DE VENTAS *** ")
        print("1-   Nueva Venta")
        print("2-   Modificar Venta")
        print("3-   Eliminar Venta")
        print("4-   Regresar a Menú Principal")
        try:
            Opc = int(input("\t>>Escoja una opción (1-4)? "))
            if Opc == 1:
                Sales = NuevaVenta(Sales, Products)
            if Opc == 2:
                Sales = ModificarVenta(Sales, Products)   
            if Opc == 3:
                Sales = EliminarVenta(Sales)
            if Opc == 4:
                UpdateProducts(Products)
                return Sales
        except ValueError:
            print("Error! Ingrese un numero entero valido")
#******************************** FUNCIONES APARTADO DE PRODUCTOS ********************************
#Función Mostrar SubMenú de Productos
def ProductsMenu(Products):
    while True:
        print("\n","=" * 40)
        print("*** SUBMENÚ DE PRODUCTOS *** ")
        print("1-   Agregar Producto")
        print("2-   Modificar Producto")
        print("3-   Eliminar Producto")
        print("4-   Regresar a Menú Principal")
        try:
            Opc = int(input("\t>>Escoja una opción (1-4)? "))
            if Opc == 1:
                Products = AgregarProducto(Products)
            if Opc == 2:
                Products = ModificarProducto(Products)
            if Opc == 3:
                Products = EliminarProducto(Products)
            if Opc == 4:
                UpdateProducts(Products)
                return Products
        except ValueError:
            print("Error! Ingrese un numero entero valido")

#Función para Agregar un nuevo Producto
def AgregarProducto(Products):
    print("\n","=" * 40)
    print("\n\f AGREGAR PRODUCTO")
    Cod = LeerString("Ingrese codigo del Producto")
    if Cod in Products:
        MsgNotify("CODIGO OCUPADO")
    else:
        Name = LeerString("Nombre del Producto: ")
        VlrUni = LeerEntero("Ingrese Valor Unitario del Producto: ")
        TypeIVA = MenuIVA()       
        Products[Cod] = {}
        Products[Cod]["Name"] = Name
        Products[Cod]["VlrUni"] = VlrUni
        Products[Cod]["IVA"] = TypeIVA  
    return Products

#Función para Modificar Producto Existente
def ModificarProducto(Products):
    print("\n","=" * 40)
    print("\n\f MODIFICAR PRODUCTO")
    Cod = LeerString("Ingrese codigo del Producto")
    if Cod in Products:
        while True:                                                         #SubMenú para Modificar Producto
            print(" DATO A MODIFICAR ")
            print("1- Nombre")                                              #1 Modificar el Nombre
            print("2- Valor Unitario")                                      #2 Modificar el valor Unitario
            print("3- Tipo de Iva")                                         #3 Modificar tipo de IVA
            print("4- Return Menu")  
            try:
                Opc = int(input("\t>>Escoja una opción (1-4)? "))
                if Opc == 1:
                    Products[Cod]["Name"] = LeerString("Ingrese nuevo nombre: ")
                    print("Nombre modificado correctamente")
                elif Opc == 2:
                    Products[Cod]["VlrUni"] = LeerEntero("Ingrese nuevo Valor Unitario: ")
                    print("Valor Unitario modificado correctamente")
                elif Opc == 3:
                    Products[Cod]["IVA"] = MenuIVA()
                    print("Tipo de IVA modificado correctamente")
                elif Opc == 4:
                    MsgNotify("PRODUCTO MODIFICADO EXITOSAMENTE")
                    return Products
                else:
                    MsgNotify("Opción no valida")
                    continue
            except ValueError:
                print("Error! Ingrese un numero entero valido")
    else:
        MsgNotify("PRODUCTO NO REGISTRADO")
        return
        

#Función para Eliminar de lista un producto Existente
def EliminarProducto(Products):
    print("\n","=" * 40)
    print("\n\f ELIMINAR PRODUCTO")
    Cod = LeerString("Ingrese codigo del Producto")
    if Cod in Products:
        Products.pop(Cod)
        MsgNotify("PRODUCTO ELIMINADO EXITOSAMENTE")
        return Products                                            #Retorna una nueva lista de Productos
    MsgNotify("PRODUCTO NO REGISTRADO")

#Función para Establecer Porcentaje de IVA a un Producto
def MenuIVA():
    Iva_Porc = (0, 0.05, 0.19)
    while True:
        print("\n","=" * 40)
        print("*** TIPO DE IVA ***")
        print("1-   Exento")
        print("2-   Bienes")
        print("3-   General")
        try:
            Opc = int(input("\t>>Escoja una opción (1-3)? "))
            if Opc > 0 and Opc < 4:
                return Iva_Porc[Opc - 1]
            MsgNotify("Opción no valida")
            continue
        except ValueError:
            print("Error! Ingrese un numero entero valido")

#******************************* FUNCIÓN IMPRIMIR DETALLES VENTA DIARIA ********************************
#Función Imprimir Detalle de ventas del Día
def DetailsACME(Sales):
    print("*" * 10, "INFORME DETALLADO DE VENTAS DEL DÍA", "*" * 10)
    print("|{:<10}|{:>15}|{:>15}|{:>15}|".format("VENDIDOS", "TOTAL SIN IVA", "TOTAL IVA", "TOTAL CON IVA"))
    TotalCant = 0
    TotalNoIVA = 0
    TotalIVA = 0
    TotalConIVA = 0
    for IDCliente in Sales.keys():
        for Cod in Sales[IDCliente].keys():
            if Cod == "TotalPagar":
                break
            TotalCant += Sales[IDCliente][Cod]["Cant"]
            TotalNoIVA += Sales[IDCliente][Cod]["VlrProd"]
            TotalIVA += Sales[IDCliente][Cod]["VlrIVA"]
            TotalConIVA += Sales[IDCliente][Cod]["VlrTotal"]    
    print("|{:<10}|{:>15,}|{:>15,}|{:>15,}|".format(TotalCant, TotalNoIVA, TotalIVA, TotalConIVA))
    print("+----------+---------------+---------------+---------------+")



#******************************** MAIN CODE ********************************


#Enseñar Menú Principal
while True:
    Opc = MainMenu()
    if Opc == 1:
        Sales = SalesMenu(Sales, Products)
    elif Opc == 2:
        Products = ProductsMenu(Products)
    elif Opc == 3:
        DetailsACME(Sales)
    elif Opc == 4:
        UpdateProducts(Products)
        UpdateSales(Sales)
        print("-" * 14)
        print(" CAJA CERRADA")
        print("-" * 14)
        break