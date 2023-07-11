'''Mi agenda telefonica con diccionarios'''

telefonos={'José':1234,
           'María':3456,
           'Andrés':5678,
           'Lucía':9876}

while True:
    print()
    title='Mis Telefonos'.center(40)
    print(title)
    print('-'*40,'\n')
    print('1.) Consultar')
    print('2.) Añadir')
    print('3.) Modificar')
    print('4.) Eliminar')
    print('5.) Salir')
    print('\n','-'*40,'\n')

    opcion=input('Digite una opcion: ')
    
    if opcion.isdigit()==False:
        print('Opción No valida...')
        continue
    elif opcion=='1':
        print('\n',telefonos)
    elif opcion=='2':
        print('\n')
        nombre=input('Digite un nombre: ')
        numero=input('Digite un telefono: ')
        if nombre.isalpha()==False:
            print('No escriba numeros en el nombre...')
            continue
        elif numero.isdigit()==False:
            print('No escriba palabras en el nombre...')
            continue
        else:
            numero=int(numero)
            telefonos[nombre]=numero
            print('Usuario Agregado...')
    elif opcion=='3':
        print('\n')
        nombre=input('Digite un nombre: ')
        if nombre.isalpha()==False:
            print('No escriba numeros en el nombre...')
            continue
        else:
            for telefono in telefonos.keys():
                if telefono==nombre:
                    print('El usuario existe...')
                    numero=input('Digite un telefono: ')
                    if numero.isdigit()==False:
                        print('No escriba palabras en el nombre...')
                        continue
                    numero=int(numero)
                    telefonos[nombre]=numero
                    print('Usuario Modificado...')
                    existencia=True
                    break
                elif telefono!=nombre:
                    existencia=False
            if existencia==False:
                print('el usuario no existe...')
            else:
                print('Saliendo...')
            
    elif opcion=='4':
        print('\n')
        nombre=input('Digite un nombre: ')
        if nombre.isalpha()==False:
            print('No escriba numeros en el nombre...')
            continue
        
        del telefonos[nombre]
        print('Usuario Eliminado...')
    elif opcion=='5':
        print('Saliendo...')
        break


