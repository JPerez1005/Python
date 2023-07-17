'''La empresa ACME desea que le construya un programa para gestionar la nómina de sus empleados. Después
de recoger los requerimientos se llegó a la decisión de gestionar los empleados y sus nóminas a través del
siguiente menú.'''

import math
empleados = []#Lista Principal

'''Agregar empleado: Esta opción permite adicionar un empleado con su id, nombre, horas trabajadas y
valor de la hora. Los empleados pueden trabajar entre 1 a 160 Horas. Y el valor de la hora puede estar
entre $8,000 y $150,000 pesos la hora.'''
# Función para agregar un empleado
def agregar_empleado():
    while True:
        try:
            id_empleado = int(input("Ingrese el ID del empleado: "))
            while True:
                nombre=input('Ingrese el nombre del empleado: ')
                if not nombre.isdigit():
                    break
                else:
                    print('No se admiten numeros...')
            while True:
                horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
                if 1<horas_trabajadas<160:
                    break
                else:
                    print('Digite una hora valida...')
            
            while True:
                valor_hora = int(input("Ingrese el valor de la hora trabajada: "))
                if 8000<valor_hora<150000:
                    break
                else:
                    print('Digite un valor valido...')

            empleado = [id_empleado, nombre, horas_trabajadas, valor_hora]#metemos las variables en una lista de empleado
            empleados.append(empleado)#la lista la implementasmos con append para que no se extienda la lista
            print("Empleado agregado correctamente.")
            return
        except ValueError:
            print('Digite un valor valido')

'''Modificar empleado: Esta opción permite cambiar cualquiera de los datos del empleado, menos el id de
empleado.'''
def modificar_empleado():
    while True:
        try:
            id_empleado = input("Ingrese el ID del empleado a modificar: ")#el usuario digita que id
            #quiere modificar

            for empleado in empleados:#por cada lista en la lista principal
                if empleado[0] == id_empleado:#si el primer valor de alguna de las listas coincide, entonces:
                    while True:
                        nombre=input('Ingrese el nuevo nombre del empleado: ')
                        if not nombre.isdigit():
                            break
                        else:
                            print('No se admiten numeros...')
                    while True:
                        horas_trabajadas = int(input("Ingrese la nueva cantidad de horas trabajadas: "))
                        if 1<horas_trabajadas<160:
                            break
                        else:
                            print('Digite una hora valida...')
                    
                    while True:
                        valor_hora = int(input("Ingrese el nuevo valor de la hora trabajada: "))
                        if 8000<valor_hora<150000:
                            break
                        else:
                            print('Digite un valor valido...')

                    empleado[1] = nombre#en cada una de las posiciones vamos asignando las nuevas variables...
                    empleado[2] = horas_trabajadas
                    empleado[3] = valor_hora
                    print("Empleado modificado correctamente.")
                    return

            print("No se encontró un empleado con el ID ingresado.")
        except ValueError:
            print('Digite un valor valido')

'''Buscar empleado: Esta opción permite buscar un empleado por su id, si lo encuentra, muestra la
información de este y si no, muestra un mensaje de que el empleado no ha sido ingresado'''
def buscar_empleado():
    while True:
        try:
            id_empleado = input("Ingrese el ID del empleado a buscar: ")

            for empleado in empleados:#por cada lista en la lista principal
                if empleado[0] == id_empleado:#si el primer valor de alguna de las listas coincide, entonces:
                    print('-'*15)
                    #MOSTRAMOS LOS DATOS DEL EMPLEADO POR POSICION
                    print("ID:", empleado[0])
                    print("Nombre:", empleado[1])
                    print("Horas trabajadas:", empleado[2])
                    print("Valor de la hora:", empleado[3])
                    print('-'*15)
                    return

            print("No se encontró un empleado con el ID ingresado.")
        except ValueError:
            print('Digite un valor valido')

'''Eliminar empleado: Esta opción permite eliminar a un empleado por su id. Si borra al empleado, muestra
un mensaje que ha sido eliminado y si no, muestra un mensaje de que no se eliminó el empleado.'''
def eliminar_empleado():
    while True:
        try:
            id_empleado = input("Ingrese el ID del empleado a eliminar: ")#el usuario ingresa un id

            for empleado in empleados:#por cada lista en la lista principal
                if empleado[0] == id_empleado:#si el primer valor de alguna de las listas coincide, entonces:
                    empleados.remove(empleado)#En la lista principal removemos la lista del empleado
                    #en la que coincide el id
                    print("Empleado eliminado correctamente.")
                    return#con return nos salimos de todo

            print("No se encontró un empleado con el ID ingresado.")
        except ValueError:
                print('Digite un valor valido')

'''Listar Empleados: Esta opción permite mostrar los empleados con su información (id, nombre, horas y
valor de la hora trabajada), debe permitir paginación, esto es, se muestran los primeros 5 empleados,
luego para y muestra un mensaje para que el usuario decida si desea seguir viendo o volver al menú. Si
desea seguir viendo, le muestra los siguientes 5 empleados y así sucesivamente hasta que no haya más
empleados o la persona no desee seguir viendo.'''
def listar_empleados():
    if len(empleados) == 0:#si en la lista princila los numeros totales cero
        #es por que no se ah digitado ningun usuario
        print("No hay empleados registrados.")
        return

    num_empleados = len(empleados)#con len calculo el total de empleados
    tam_pagina = 5#un limite para mostrar
    num_paginas = math.ceil(num_empleados / tam_pagina)#hacemos un redondeo,
    #Dividimos el numero de empleados con el tamaño de la pag, y nos da el total de paginas
    pagina_actual = 1
    indice_inicial = 0

    while pagina_actual <= num_paginas:#mientras que la pag actual sea menor al totl de pags que hay
        print("=== Página", pagina_actual, "===")#nos muestra en pag que vamos
        empleados_pagina = empleados[indice_inicial:indice_inicial+tam_pagina]
        #Creamos nueva variable, de la lista principal que inicie de [0:5]
        for empleado in empleados_pagina:
            #empleados pagina solo va de 0:5
            print("ID:", empleado[0])#mostramos cada posicion de la sublista etc...
            print("Nombre:", empleado[1])
            print("Horas trabajadas:", empleado[2])
            print("Valor de la hora:", empleado[3])
            print("-------------------")

        if pagina_actual < num_paginas:#verificamos si hay mas paginas
            respuesta = input("Presione Enter para ver los siguientes empleados o ingrese 'M' para volver al menú: ")
            if respuesta.lower() == "m":#si el usuario ingresa m nos salimos
                break

        pagina_actual += 1#La pagina actual aumenta a uno
        indice_inicial += tam_pagina
        #indice inicial suma el tamaño de pagina


'''Listar la nómina de un empleado: Esta opción permite mostrar la nómina de un empleado buscado por
su ID. El salario bruto se calcula como el valor de la hora por la cantidad de horas trabajadas. Si gana
menos del salario mínimo legal vigente en Colombia 2023 (por favor consulte el dato) se le debe da
subsidio de transporte. Se le debe descontar el valor de la eps y pensión correspondiente al 4% cada uno
y el salario Neto es la suma del salario bruto, el auxilio menos los descuentos.
El menú debe mostrar los datos del empleado y los datos de la nómina.'''
def calcular_nomina_empleado():
    id_empleado = input("Ingrese el ID del empleado: ")

    for empleado in empleados:
        if empleado[0] == id_empleado:#si el id coincide se hacen los calculos
            horas_trabajadas = empleado[2]#guardamos las horas trabajadas
            valor_hora = empleado[3]#guardamos el valor de la hora
            salario_bruto = horas_trabajadas * valor_hora#multiplicamos hora por valor
            salario_minimo = 1160000  # Salario mínimo legal vigente en Colombia para el año 2023
            auxilio_transporte = 140606  # Auxilio de transporte para el año 2023
            eps = salario_bruto * 0.04#eps 4%
            pension = salario_bruto * 0.04#pension 4%
            salario_neto = salario_bruto - eps - pension#salario bruto menos los descuentos

            print("ID:", empleado[0])
            print("Nombre:", empleado[1])
            print("Horas trabajadas:", horas_trabajadas)
            print("Valor de la hora:", valor_hora)
            print("Salario bruto:", salario_bruto)
            if salario_bruto < salario_minimo:#si salario bruto es menor al salario minimo
                print("Auxilio de transporte:", auxilio_transporte)#se le da un auxilio de transporte
            print("EPS:", eps)
            print("Pensión:", pension)
            print("Salario neto:", salario_neto)
            print("-------------------")

            return

    print("No se encontró un empleado con el ID ingresado.")


'''Listar nómina de todos los empleados: Esta opción permite mostrar la nómina de todos los empleados.
El listado debe estar paginado cada 5 empleados. El calculo de la nómina de cada empleado es el mismo
que en la opción 6.'''
def listar_nomina_empleados():
    if len(empleados) == 0:#lo mismo si no hay usuarios me dice q no hay
        print("No hay empleados registrados.")
        return

    #se usa el mismo paso de paginas anterior
    num_empleados = len(empleados)
    tam_pagina = 5
    num_paginas = math.ceil(num_empleados / tam_pagina)
    pagina_actual = 1
    indice_inicial = 0

    while pagina_actual <= num_paginas:
        print("=== Página", pagina_actual, "===")#indica la pagina actual
        empleados_pagina = empleados[indice_inicial:indice_inicial+tam_pagina]

        for empleado in empleados_pagina:
            print("ID:", empleado[0])
            print("Nombre:", empleado[1])
            horas_trabajadas = empleado[2]
            valor_hora = empleado[3]
            salario_bruto = horas_trabajadas * valor_hora
            salario_minimo = 1160000  # Salario mínimo legal vigente en Colombia para el año 2023
            auxilio_transporte = 140606  # Auxilio de transporte para el año 2023
            eps = salario_bruto * 0.04
            pension = salario_bruto * 0.04
            salario_neto = salario_bruto - eps - pension

            print("Salario bruto:", salario_bruto)
            if salario_bruto < salario_minimo:
                print("Auxilio de transporte:", auxilio_transporte)
            print("EPS:", eps)
            print("Pensión:", pension)
            print("Salario neto:", salario_neto)
            print("-------------------")

        if pagina_actual < num_paginas:
            respuesta = input("Presione Enter para ver los siguientes empleados o ingrese 'M' para volver al menú: ")
            if respuesta.lower() == "m":
                break

        pagina_actual += 1
        indice_inicial += tam_pagina


# Función principal del programa
def main():
    while True:
        print("*** NOMINA ACME ***")
        print("MENU")
        print("1- Agregar empleado")
        print("2- Modificar empleado")
        print("3- Buscar empleado")
        print("4- Eliminar empleado")
        print("5- Listar empleados")
        print("6- Listar nómina de un empleado")
        print("7- Listar nómina de todos los empleados")
        print("8- Salir")
        opcion = input("Escoja una opción (1-8): ")

        if opcion == "1":
            agregar_empleado()
        elif opcion == "2":
            modificar_empleado()
        elif opcion == "3":
            buscar_empleado()
        elif opcion == "4":
            eliminar_empleado()
        elif opcion == "5":
            listar_empleados()
        elif opcion == "6":
            calcular_nomina_empleado()
        elif opcion == "7":
            listar_nomina_empleados()
        elif opcion == "8":
            confirmacion = input("¿Está seguro de que desea salir? (S/N): ")
            if confirmacion.lower() == "s":
                print("Gracias por utilizar el programa. ¡Hasta luego!")
                break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

# Ejecutar el programa
main()