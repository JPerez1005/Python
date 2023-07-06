'''La empresa ACME desea que le construya un programa para gestionar la nómina de sus empleados. Después
de recoger los requerimientos se llegó a la decisión de gestionar los empleados y sus nóminas a través del
siguiente menú.'''
lista=[]
AgregarE=[]
'''Agregar empleado: Esta opción permite adicionar un empleado con su id, nombre, horas trabajadas y
valor de la hora. Los empleados pueden trabajar entre 1 a 160 Horas. Y el valor de la hora puede estar
entre $8,000 y $150,000 pesos la hora.'''

def AgregarEmpleado():
    Id=int(input('Digite id del empleado: '))
    Nombre=input('Digite nombre del empleado: ')
    while True:
        HorasT=int(input('Digite las horas trabajadas: '))
        if 1<HorasT<160:
            break
        else:
            print('Digite horas validas')
            continue
    
    while True:
        ValorH=int(input('Digite el valor de hora del empleado: '))
        if 8000<ValorH<150000:
            break
        else:
            print('Digite valor valido')
            continue
    Todo=(Id,Nombre,HorasT,ValorH)
    AgregarE.extend(Todo)
    lista.append(AgregarE)
    print(lista)

'''Modificar empleado: Esta opción permite cambiar cualquiera de los datos del empleado, menos el id de
empleado.'''


def ModificarEmpleado(posicion):
    Nombre=input('Digite el nuevo nombre del empleado: ')
    while True:
        HorasT=int(input('Digite las nuevas horas trabajadas: '))
        if 1<HorasT<160:
            break
        else:
            print('Digite horas validas')
            continue
    while True:
        ValorH=int(input('Digite el valor de hora del empleado: '))
        if 8000<ValorH<150000:
            break
        else:
            print('Digite valor valido')
            continue
    Todo=(Nombre,HorasT,ValorH)
    AgregarE.extend(Todo)
    lista[posicion]=AgregarE
    print(lista)


'''Buscar empleado: Esta opción permite buscar un empleado por su id, si lo encuentra, muestra la
información de este y si no, muestra un mensaje de que el empleado no ha sido ingresado'''
def BuscarEmpleado(idIgual):
    for elem in range(len(lista)):
        for valor in range(len(AgregarE)):
            if AgregarE[0]==idIgual:
                print(AgregarE[valor])
    return 'No se encontró'      


'''Eliminar empleado: Esta opción permite eliminar a un empleado por su id. Si borra al empleado, muestra
un mensaje que ha sido eliminado y si no, muestra un mensaje de que no se eliminó el empleado.'''
def EliminarEmpleado(idIgual):
    for elem in range(len(lista)):
        for valor in range(len(AgregarE)):
            if AgregarE[0]==idIgual:
                print(AgregarE[valor])
                Desicion=input('Usuario Encontrado, Dese eliminarlo?: ')
                if Desicion.lower()=='si':
                    lista.pop(elem)
                    print('Usuario Eliminado...')
                    break
                else:
                    print('No se eliminó el usuario...')
                    break
    return 'No se encontró'  

'''Listar Empleados: Esta opción permite mostrar los empleados con su información (id, nombre, horas y
valor de la hora trabajada), debe permitir paginación, esto es, se muestran los primeros 5 empleados,
luego para y muestra un mensaje para que el usuario decida si desea seguir viendo o volver al menú. Si
desea seguir viendo, le muestra los siguientes 5 empleados y así sucesivamente hasta que no haya más
empleados o la persona no desee seguir viendo.'''
def ListarEmpleados():
    # Obtener la longitud de la lista de empleados
    num_empleados = len(lista)
    # Definir el tamaño de la página (cantidad de empleados por página)
    tam_pagina = 5
    # Inicializar el índice inicial
    indice_inicial = 0

    while indice_inicial < num_empleados:
        # Obtener el índice final de la página actual
        indice_final = indice_inicial + tam_pagina
        # Obtener la lista de empleados para la página actual
        empleados_pagina = lista[indice_inicial:indice_final]

        # Mostrar los empleados de la página actual
        for empleado in empleados_pagina:
            print(empleado)

        # Verificar si hay más empleados o si el usuario desea seguir viendo
        if indice_final < num_empleados:
            respuesta = input("Presione Enter para ver los siguientes empleados o ingrese 'M' para volver al menú: ")
            if respuesta.lower() == "m":
                break

        # Actualizar el índice inicial para la siguiente página
        indice_inicial = indice_final


'''Listar la nómina de un empleado: Esta opción permite mostrar la nómina de un empleado buscado por
su ID. El salario bruto se calcula como el valor de la hora por la cantidad de horas trabajadas. Si gana
menos del salario mínimo legal vigente en Colombia 2023 (por favor consulte el dato) se le debe da
subsidio de transporte. Se le debe descontar el valor de la eps y pensión correspondiente al 4% cada uno
y el salario Neto es la suma del salario bruto, el auxilio menos los descuentos.
El menú debe mostrar los datos del empleado y los datos de la nómina.'''
def ListarNominaDeUnEmpleado():
    pass

def ListarNominaDeTodosLosEmpleados():
    pass

#MARCA ACME
def LeerInt(msg):
    while True:
        try:
            n=int(input(msg))
            return n#Se sale de todo
        except ValueError:
            print('Error!. Ingrese un numero entero valido.')

def msgError(msg):
    print('¡Error!', msg)
    input('Presione Cualquier tecla para continuar...')

def Menu():
    while True:
        print('\n','*'*5 )
        print(' MENU ')
        print('*'*5 ,'\n')
        print('1.) Agregar empleado')
        print('2.) ModificarEmpleado')
        print('3.) BuscarEmpleado')
        print('4.) EliminarEmpleado')
        print('5.) ListarEmpleados')
        print('6.) ListarNominaDeUnEmpleado')
        print('7.) Salir...')
        op=LeerInt('\n>> Opción (1 a 7): ')
        if op<1 or op>7:
            msgError('Opcion no valida')
            continue
        return op

#PROGRAMA GENERAL
while True:
    opcion=Menu()

    if opcion==1:
        AgregarEmpleado()
    elif opcion==2:
        posicion=int(input('Digite la posicion a modificar: '))
        ModificarEmpleado(posicion)
    elif opcion==3:
        idIgual=int(input('Digite el id que desea buscar: '))
        BuscarEmpleado(idIgual)
    elif opcion==4:
        idIgual=int(input('Digite el id que desea eliminar: '))
        EliminarEmpleado(idIgual)
    elif opcion==5:
        ListarEmpleados()
    elif opcion==6:
        ListarNominaDeUnEmpleado()
    elif opcion==7:
        print('\n**Gracias por usar la mini calculadora**\n')
        break
    else:
        msgError('Opcion Invalida.')