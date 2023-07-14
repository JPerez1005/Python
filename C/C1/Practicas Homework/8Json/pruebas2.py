import json

empleado={}
def AgregarEmpleado():
    id = input("Ingrese el id del empleado: ")
    nombre = input("Ingrese el nombre de empleado: ")
    horas = int(input("Ingrese horas trabajadas: "))
    while True:
        if horas < 1 or horas > 160:
            print("Ingrese una hora valida")
            return horas
        else:
            break

    while True:
        valorhora = int(input("Ingrese el valor de la hora trabajada: "))

        if valorhora < 8000 or valorhora > 150000:
            print("Ingrese un valor de hora adecuado")

        else:
            break

    # Guardar en el disco
    
    empleado[id]={
        "nombre":nombre,
        "Horas trabajadas":str(horas),
        "Valor horas":str(valorhora)
    }
    with open('emplacme.json','w') as archivo:
        archivo.write('{')
        archivo.write('\n')
        archivo.write(f'"usuarios":')
        json.dump(empleado, archivo)
        archivo.write('\n')
        archivo.write('}')

def escribirMemDisco(empleado):
    with open('emplacme.json','w') as archivo:
        

        for id in empleado.keys():
            nombre = empleado[id]["nombre"]
            horastrab = empleado[id]["Horas trabajadas"]
            valhora = empleado[id]["Valor horas"]
            empleado[id]={
                "nombre":nombre,
                "Horas trabajadas":str(horastrab),
                "Valor horas":str(valhora)
            }
            archivo.write('{')
            archivo.write('\n')
            archivo.write(f'"{id}":')
            json.dump(empleado, archivo)
            archivo.write('\n')
            archivo.write('}')


def ModificarEmpleado():
    while True:
        buscarid = input("Ingrese el id del empleado que desea modificar: ")
        if buscarid in empleado:
            print("ID ENCONTRADO")
            modificar = int(input("Ingrese un numero: "))
            if modificar == 1:
                nombrenuevo = input("Ingrese el nuevo nombre: ")
                empleado[buscarid]["nombre"] = nombrenuevo
                break
            elif modificar == 2:
                nuevahora = int(input("Ingrese las nuevas horas trabajadas: "))
                empleado[buscarid]["Horas trabajadas"] = nuevahora
                break
            elif modificar == 3:
                nuevovalorh = int(input("Ingrese nuevo valor trabajadas: "))
                empleado[buscarid]["Valor horas"] = nuevovalorh
                break
            else:
                print("Ingrese un numero valido")
        else:
            ("ID NO ENCONTRADO")
    
    escribirMemDisco(empleado)


def BuscarEmpleados():
    with open('emplacme.json','r') as archivo:
        Diccionario=json.load(archivo)#leo el archivo internamente
    
    print('diccionario: ',Diccionario)

def EliminarEmpleados():
    while True:
        buscarid = input("Ingrese el id del empleado que desea eliminar : ")
        if buscarid in empleado:
            empleado.pop(buscarid)
            print(f"ID ELIMINADO,se elimino el id : {buscarid}")
            break
        print("El id ingresado no existe ingrese de nuevo ")

    escribirMemDisco()
    input("---> Presione ENTER para continuar")

def mostrarEmpleado():
    idBusqueda=input('Digite el id: ')
    with open('emplacme.json','r') as archivo:
        Diccionario=json.load(archivo)#leo el archivo internamente
        print(Diccionario["usuarios"])
        if Diccionario["usuarios"]==idBusqueda:
            print('Usuario: ',Diccionario["usuarios"][idBusqueda]["nombre"])
            print()
    
    #print('diccionario: ',Diccionario)

def ListarNominaEmpleado():
    while True:
        buscarid = input("Ingrese el id del empleado que desea modificar: ")
        if buscarid in empleado:
            print("ID ENCONTRADO")
            break
        else:
            print("ID NO ENCONTRADO")

    sueldobruto = empleado[buscarid]["Horas trabajadas"] * \
        empleado[buscarid]["Valor horas"]
    eps = sueldobruto * 0.04
    pension = sueldobruto * 0.04
    descuento = (eps + pension)
    auxilio = 0
    nombre = empleado[buscarid]["nombre"]
    if sueldobruto <= 1160000:
        print("Merecedor subsidio de transporte")
        auxilio = 140606
    sueldoneto = (sueldobruto + auxilio) - descuento
    print(f"La nomina del empleado {nombre}")
    print(f"Sueldo bruto: {sueldobruto}")
    print(f"Valor eps: {eps}")
    print(f"Valor pension: {pension}")
    print(f"Valor auxilio: {auxilio}")
    print(f"Sueldo neto: {sueldoneto}")
    input("---> Presione ENTER para continuar")

def ListarNominaEmpleados():
    pass


def mostrar_menu():
    #cargarArch()
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
        print("--------------------")

        if opcion == "1":
            AgregarEmpleado()
        elif opcion == "2":
            ModificarEmpleado()
        elif opcion == "3":
            BuscarEmpleados()
        elif opcion == "4":
            EliminarEmpleados()
        elif opcion == "5":
            mostrarEmpleado()
        elif opcion == "6":
            ListarNominaEmpleado()
        elif opcion == "7":
            ListarNominaEmpleados()
        elif opcion == "8":
            confirmacion = input("¿Está seguro de que desea salir? (S/N): ")
            if confirmacion.upper() == "S":
                print("¡Hasta luego!")
                break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
        print("--------------------")

# Ejecutar el programa
mostrar_menu()