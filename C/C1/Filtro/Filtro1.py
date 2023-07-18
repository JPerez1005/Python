'''Recordar subir al github dejar el comentario link y subirlo al classroom

Se hace uso de reportes

-Se hace menu de gestion de tarjetas
-Se hace menu de gestion de clientes
'''

import json
import io
import os
#------------------------------------------------------------------------------------------
# Función para abrir el archivo de datos
def CargarDatos(NombreArchivo):
    try:
        with open(NombreArchivo, 'r') as archivo:
            contenido = json.load(archivo)
    except FileNotFoundError:
        contenido = []
    return contenido

#Funcion de Limpieza
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Función para guardar el archivo de datos
def Actualizar(NombreArchivo, contenido):
    with open(NombreArchivo, 'w') as archivo:
        json.dump(contenido, archivo)

Archivo='ClientesBanco.json'#creamos el archivo
# Abrir el archivo y cargar los datos existentes
contenidoBanco = CargarDatos(Archivo)
#en contenido se muestran los datos de ese archivo




#----------------------------------------------------------------------------------------
#Agregar Cliente
'''Las tarjetas de crédito son emitidas a clientes del banco. La información que
se necesita registrar de los clientes es:
    ▪ Nombre del cliente
    ▪ Cedula de Ciudadanía
    ▪ Número de teléfono de contacto
    ▪ Sexo'''
def AgregarCliente():
    print('-'*5,'Este es el registro de clientes','-'*5)
    ID = input('ID del cliente: ')
    if ID.isalpha():
        print('No digite letras...')
        return
    for cliente in contenidoBanco:
        if cliente['id']==ID:
            print('Ese id ya existé')
            return
    Nombre = input('Nombre del cliente: ')
    if Nombre.isdigit():
        print('No digite numeros...')
        return
    NumTelefono = input('Numero Telefonico del cliente: ')
    if NumTelefono.isalpha():
        print('No digite letras...')
        return
    Sex=input('Sexo del cliente(m/f): ')
    if Sex.lower().strip()!='m':
        if Sex.lower().strip()!='f':
            print('Solo son validos (f) y (m)')

    cliente = {
        'nombre': Nombre,
        'id': ID,
        'numero de telefono': NumTelefono,
        'sexo':Sex,
        'Tarjetas':[]
    }
    contenidoBanco.append(cliente)
    print('Cliente agregado correctamente.')

#----------------------------------------------------------------------------------------
#Menu Tarjeta
'''✓ La información de las tarjetas de crédito es:
    ▪ El tipo de tarjeta (Master Card, Visa, Américan Express)
    ▪ El número de la tarjeta de crétido
    ▪ Mes y año de validez
    ▪ Código de verificación (número entero de tres dígitos entre 100 y
    999)
    ▪ Id del cliente del banco dueño de la tarjeta'''

def AgregarTarjeta():
    print('--- Realizar Registro ---')
    id_cliente = input('Cedula del cliente: ')#el usuario coloca el id,

    cliente = next((c for c in contenidoBanco if c['id'] == id_cliente), None)
    if cliente is None:#si no existe el id entonces...
        print('Cliente no encontrado. Registro Cancelado.')
        print('Puede Agregar el cliente en la opción de agregar cliente')
        return
    Tarjetas=[]
    TT=''
    print('Ingrese la información de las tarjetas:')
    while True:
        print('Si desea salir del programa digite fin')
        TipoTarjeta = input('Tipo de Tarjeta (1: Master Card, 2: Visa, 3: Américan Express): ')
        if TipoTarjeta.lower().strip() == 'fin':#si el usuario digita fin se sale
            return
        if TipoTarjeta.isalpha():
            print('No se Permite el ingreso de letras...')
            return
        if TipoTarjeta=='1':
            TT='Master Card'
        elif TipoTarjeta=='2':
            TT='Visa'
        elif TipoTarjeta=='3':
            TT='Américan Express'
        else:
            print('No tenemos convenio con esa Tarjeta...')
            return
        NumTarjeta=0
        NumTarjeta = input('Numero de Tarjeta de credito a registrar: ')
        if NumTarjeta=='':
            print('El numero de la tarjeta no puede ser vacía')
            return
        for cliente in contenidoBanco:
            CantidadTarjetas=len(cliente['Tarjetas'])
            for i in range(0, CantidadTarjetas):
                if NumTarjeta==cliente['Tarjetas'][i]['Numero de Tarjeta']:
                    print('esa tarjeta ya existe')
                    return
        Mes=input('Digite Mes de Validez: ')
        Anio=input('Digite año de validez: ')
        if Mes.isalpha() or Anio.isalpha():
            print('No digite letras en los meses y años')
            return
        if Mes=='' or Anio=='':
            print('No digitó Valores en los meses y años')
            return
        try:
            CodVer=int(input('Código de verificación (número entero de tres dígitos entre 100 y 999):'))
            if CodVer>100:
                if CodVer<999:
                    print()
                else:
                    print('Ese numero no está dentro de los parametros indicados...')
                    return
            else:
                print('Ese numero no está dentro de los parametros indicados...')
                return
        except ValueError:
            print('Codigo de verificación no valido...')
            return
        #colocamos todos los valores en el diccionario
        Tarjeta = {
            'Tipo de Tarjeta': TT,
            'Numero de Tarjeta': NumTarjeta,
            'Año y mes de validez': [Anio,Mes],
            'Codigo de Verificación': CodVer,
            'Cedula del cliente': id_cliente
        }
        
        #enlistamos todos los productos al final
        Tarjetas.append(Tarjeta)
        break
    cliente['Tarjetas'].extend(Tarjetas)

'''✓ El sistema debe permitir el añadir, modificar, eliminar, borrar y hacer
reportes de las tarjetas de créditos emitidas.'''
def ModificarTarjeta():
    print('--- Modificar Tarjeta ---')
    numTarjeta=input('Digite el numero de la tarjeta de credito: ')
    if numTarjeta.isalpha():
        print('No digite letras...')
        return
    existente=True
    for cliente in contenidoBanco:
        for i in range(0,len(cliente['Tarjetas'])):
            if cliente['Tarjetas'][i]['Numero de Tarjeta'] == numTarjeta:
                print('Tarjeta encontrada. Datos actuales:')
                print('ID:', cliente['id'])
                print('Nombre:', cliente['nombre'])
                print('Numero de Tarjeta:',numTarjeta)
                print('Tipo de Tarjeta:',cliente['Tarjetas'][i]['Tipo de Tarjeta'])
                print('Numero de Tarjeta:',cliente['Tarjetas'][i]['Numero de Tarjeta'])
                print('Año y mes de validez:',cliente['Tarjetas'][i]['Año y mes de validez'])
                print('Codigo de Verificación:',cliente['Tarjetas'][i]['Codigo de Verificación'])
                print('Cedula del cliente:',cliente['Tarjetas'][i]['Cedula del cliente'])
                print()
                var='¡¡IMPORTANTE!!'
                print('{:^}'.format(var))
                print('Si desea conservar algunos datos deje en blanco donde no quiere cambio')
                print()
                TipoTarjeta = input('Nuevo Tipo de Tarjeta (1: Master Card, 2: Visa, 3: Américan Express): ')
                if TipoTarjeta.lower().strip() == 'fin':#si el usuario digita fin se sale
                    return
                if TipoTarjeta.isalpha():
                    print('No se Permite el ingreso de letras...')
                    return
                if TipoTarjeta=='1':
                    TT='Master Card'
                elif TipoTarjeta=='2':
                    TT='Visa'
                elif TipoTarjeta=='3':
                    TT='Américan Express'
                NumTarjeta = input('Numero de Tarjeta de credito a registrar: ')
                for cliente in contenidoBanco:
                    CantidadTarjetas=len(cliente['Tarjetas'])
                    for i in range(0, CantidadTarjetas):
                        if NumTarjeta==cliente['Tarjetas'][i]['Numero de Tarjeta']:
                            print('esa tarjeta ya existe')
                            return
                Mes=input('Digite Mes de Validez: ')
                Anio=input('Digite año de validez: ')
                if Mes.isalpha() or Anio.isalpha():
                    print('No digite letras en los meses y años')
                    return
                try:
                    CodVer=int(input('Código de verificación (número entero de tres dígitos entre 100 y 999):'))
                    if CodVer>100:
                        if CodVer<999:
                            print()
                        else:
                            print('Ese numero no está dentro de los parametros indicados...')
                            return
                    else:
                        print('Ese numero no está dentro de los parametros indicados...')
                        return
                except ValueError:
                    print('Codigo de verificación no valido...')
                    return
                

                if TT:
                    cliente['Tarjetas'][i]['Tipo de Tarjeta'] = TT
                if NumTarjeta:
                    cliente['Tarjetas'][i]['Numero de Tarjeta'] = NumTarjeta
                if Mes:
                    cliente['Tarjetas'][i]['Año y mes de validez'][1] = Mes
                if Anio:
                    cliente['Tarjetas'][i]['Año y mes de validez'][0]= Anio
                if CodVer:
                    cliente['Tarjetas'][i]['Codigo de Verificación'] = CodVer
                print('Cliente modificado correctamente.')
                break
            else:
                existente=False
    if existente==False:
        print('No se encontró el usuario')

def EliminarTarjeta():
    print('--- Modificar Tarjeta ---')
    numTarjeta=input('Digite el numero de la tarjeta de credito: ')
    if numTarjeta.isalpha():
        print('No digite letras...')
        return
    existente=True
    for cliente in contenidoBanco:
        for i in range(0,len(cliente['Tarjetas'])):
            if cliente['Tarjetas'][i]['Numero de Tarjeta'] == numTarjeta:
                print(i)
                print('La tarjeta existe.')
                #cliente['Tarjetas'][i].clear()
                #cliente['Tarjetas'].clear()
                cliente['Tarjetas'].remove(cliente['Tarjetas'][i])
                Actualizar(Archivo, contenidoBanco)
                print('Ahora ya no :)')
                existente=True
                return
            else:
                existente=False
    if existente==False:
        print('Esa tarjeta nunca existió')

def BuscarTarjeta():
    numTarjeta=input('Digite el numero de la tarjeta de credito: ')
    if numTarjeta.isalpha():
        print('No digite letras...')
        return
    cont=0
    for cliente in contenidoBanco:
        CantidadTarjetas=len(cliente['Tarjetas'])
        for i in range(0, CantidadTarjetas):
            if numTarjeta==cliente['Tarjetas'][i]['Numero de Tarjeta']:
                if cont==0:
                    print(f'El dueño de esa tarjeta es: {cliente["nombre"]}')
                    print(f'La cedula del cliente es: {cliente["id"]}')
                    print('El contacto es: {}'.format(cliente['numero de telefono']))
                    print('El sexo del cliente es: {}'.format(cliente['sexo']))
                    print('-'*30)
                    cont+=1
                print('Tipo de Tarjeta:',cliente['Tarjetas'][i]['Tipo de Tarjeta'])
                print('Numero de Tarjeta:',cliente['Tarjetas'][i]['Numero de Tarjeta'])
                print('Año y mes de validez:',cliente['Tarjetas'][i]['Año y mes de validez'])
                print('Codigo de Verificación:',cliente['Tarjetas'][i]['Codigo de Verificación'])
                print('Cedula del cliente:',cliente['Tarjetas'][i]['Cedula del cliente'])
                print('-'*30)
                print()

def MenuTarjeta():
    clear()
    while True:
        print('---TARJETAS CREDITO ACME---')
        print('---Area de información---')
        print('1. Agregar Tarjeta.')
        print('2. Modificar Tarjeta.')
        print('3. Eliminar Tarjeta.')
        print('4. Buscar Tarjeta.')
        print('5. Salir.')

        opcion = input('Seleccione una opción: ')
        if opcion.isalpha():
            print('No digite letras')
            continue
        if opcion == '1':
            AgregarTarjeta()
            print()
        elif opcion == '2':
            ModificarTarjeta()
            print()
        elif opcion == '3':
            EliminarTarjeta()
            print()
        elif opcion == '4':
            BuscarTarjeta()
            print()
        elif opcion == '5':
            print()
            break
        else:
            print('Opción inválida. Por favor, seleccione nuevamente.')

    print('¡Hasta luego!')
#----------------------------------------------------------------------------------------
#Informes
'''▪ Tarjetas de crédito de un cliente. Este informe emite el id del cliente,
    su nombre y la información de las tarjetas de crédito registradas a su
    nombre.'''
def MostrarTarjetasDeUsuarios():
    print(f'Lista de Tarjetas junto con el cliente')
    ide=input('Digite el id del usuario:')
    if ide.isalpha():
        print('no digite letras')
        print()
        return
    for cliente in contenidoBanco:
        if ide==cliente['id']:
            print('-'*30)
            print('Cedula:',cliente['id'])
            print('Nombre:',cliente['nombre'])
            CantidadTarjetas=len(cliente['Tarjetas'])
            for i in range(0, CantidadTarjetas):
                print('Tipo de Tarjeta:',cliente['Tarjetas'][i]['Tipo de Tarjeta'])
                print('Numero de Tarjeta:',cliente['Tarjetas'][i]['Numero de Tarjeta'])
                print('Año y mes de validez:',cliente['Tarjetas'][i]['Año y mes de validez'])
                print('Codigo de Verificación:',cliente['Tarjetas'][i]['Codigo de Verificación'])
                print('Cedula del cliente:',cliente['Tarjetas'][i]['Cedula del cliente'])

'''▪ Información de una tarjeta de crédito. Dado el número de la tarjeta de
    crédito, el informe muestra toda la información de la tarjeta,
    incluyendo la información del cliente que la tiene asociada.'''
def MostrarTarjetaDeUsuario():
    numTarjeta=input('Digite el numero de la tarjeta de credito: ')
    if numTarjeta.isalpha():
        print('No digite letras...')
        return
    cont=0
    for cliente in contenidoBanco:
        CantidadTarjetas=len(cliente['Tarjetas'])
        for i in range(0, CantidadTarjetas):
            if numTarjeta==cliente['Tarjetas'][i]['Numero de Tarjeta']:
                if cont==0:
                    print(f'El dueño de esa tarjeta es: {cliente["nombre"]}')
                    print(f'La cedula del cliente es: {cliente["id"]}')
                    print('El contacto es: {}'.format(cliente['numero de telefono']))
                    print('El sexo del cliente es: {}'.format(cliente['sexo']))
                    print('-'*30)
                    cont+=1
                print('Tipo de Tarjeta:',cliente['Tarjetas'][i]['Tipo de Tarjeta'])
                print('Numero de Tarjeta:',cliente['Tarjetas'][i]['Numero de Tarjeta'])
                print('Año y mes de validez:',cliente['Tarjetas'][i]['Año y mes de validez'])
                print('Codigo de Verificación:',cliente['Tarjetas'][i]['Codigo de Verificación'])
                print('Cedula del cliente:',cliente['Tarjetas'][i]['Cedula del cliente'])
                print('-'*30)
                print()

'''▪ Listado de tarjetas de crédito. Este informe lista la siguiente
    información de las tarjetas de crédito. El número de la tarjeta, fecha
    de vencimiento (mes/año), tipo de tarjeta, el número de
    identificación del cliente y el nombre del cliente.'''
def ListadoTarjetas():
    for cliente in contenidoBanco:
        print('-'*30)
        CantidadTarjetas=len(cliente['Tarjetas'])
        if CantidadTarjetas==0:
            continue
        for i in range(0, CantidadTarjetas):
            print('Tipo de Tarjeta:',cliente['Tarjetas'][i]['Tipo de Tarjeta'])
            print('Numero de Tarjeta:',cliente['Tarjetas'][i]['Numero de Tarjeta'])
            print('Fecha de Vencimiento:',cliente['Tarjetas'][i]['Año y mes de validez'])
            print('Codigo de Verificación:',cliente['Tarjetas'][i]['Codigo de Verificación'])
            print('Cedula del cliente:',cliente['Tarjetas'][i]['Cedula del cliente'])
        print('Cedula:',cliente['id'])
        print('Nombre:',cliente['nombre'])
        print()

'''▪ Listado de los clientes con tarjetas de crédito. Este informe lista la
    información de los clientes: Cédula, nombre y teléfono.'''
def ListadoClientesConTarjeta():
    print('Todos los clientes que tiene tarjetas de credito')
    print()
    for cliente in contenidoBanco:
        CantidadTarjetas=len(cliente['Tarjetas'])
        if CantidadTarjetas==0:
            continue
        print(f'La cedula del cliente es: {cliente["id"]}')
        print(f'El dueño de esa tarjeta es: {cliente["nombre"]}')
        print('El contacto es: {}'.format(cliente['numero de telefono']))
        print('-'*30)

'''▪ Cantidad de tarjetas de cierto tipo. Este listado muestra la cantidad
    (número) de tarjetas de cierto tipo (Master, Visa o American Express)'''
def CantTiposDeTarjeta():
    print('Cantidades de Tipos de Tarjetas')
    print()
    cont1=0
    cont2=0
    cont3=0
    for cliente in contenidoBanco:
        CantidadTarjetas=len(cliente['Tarjetas'])
        if CantidadTarjetas==0:
            continue
        for i in range(0, CantidadTarjetas):
            if cliente['Tarjetas'][i]['Tipo de Tarjeta']=='Master Card':
                cont1+=1
                continue
            elif cliente['Tarjetas'][i]['Tipo de Tarjeta']=='Visa':
                cont2+=1
                continue
            elif cliente['Tarjetas'][i]['Tipo de Tarjeta']=='Américan Express':
                cont3+=1
                continue
            else:
                print('Error')
    print()
    print('Cantidad de Tarjetas de Master Cad: {}'.format(cont1))
    print()
    print('Cantidad de Tarjetas de Visa: {}'.format(cont2))
    print()
    print('Cantidad de Tarjetas de Américan Express: {}'.format(cont3))
    print()
    pass

def Informes():
    clear()
    while True:
        print('---TARJETAS CREDITO ACME---')
        print('---Area de información---')
        print('1. Buscar Tarjeta de credito con id.')
        print('2. Buscar una Tarjeta de credito con numero de tarjeta.')
        print('3. Listado De Tarjetas que hay.')
        print('4. Listado de clientes con tarjeta.')
        print('5. Cantidades de tipos de tarjetas.')
        print('6. Salir.')

        opcion = input('Seleccione una opción: ')
        if opcion == '1':
            MostrarTarjetasDeUsuarios()
            print()
        elif opcion == '2':
            MostrarTarjetaDeUsuario()
            print()
        elif opcion == '3':
            ListadoTarjetas()
            print()
        elif opcion == '4':
            ListadoClientesConTarjeta()
            print()
        elif opcion == '5':
            CantTiposDeTarjeta()
            print()
        elif opcion == '6':
            break
        else:
            print('Opción inválida. Por favor, seleccione nuevamente.')

    print('¡Hasta luego!')

#-----------------------------------------------------------------------------------------
# Menú principal del programa
def menu():
    clear()
    while True:
        print()
        print()
        print('IMPORTANTE:los datos no se guardan hasta que se salga del programa')
        print()
        print('---TARJETAS CREDITO ACME---')
        print('1. Ingresar Cliente')
        print('2. Gestión Tarjetas Bancarias')
        print('3. Informes')
        print('4. Salir')

        opcion = input('Seleccione una opción: ')
        if opcion.isalpha():
            print('No digite letras')
            continue
        if opcion == '1':
            AgregarCliente()
            print()
        elif opcion == '2':
            MenuTarjeta()
            print()
        elif opcion == '3':
            Informes()
            print()
        elif opcion == '4':
            # Guardar los productos y clientes en los archivos antes de salir
            print('SALIENDO...')
            Actualizar(Archivo, contenidoBanco)
            break
        else:
            print('Opción inválida. Por favor, seleccione nuevamente.')

    print('¡Hasta luego!')

menu()
