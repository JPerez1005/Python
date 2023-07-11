'''Mi agenda telefonica con diccionarios'''

telefonos={'José':1234,
           'María':3456,
           'Andrés':5678,
           'Lucía':9876}

consultando=True

while consultando:
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

    opcion=''
    while opcion not in ('1','2','3','4','5'):
        opcion=input('-> ')
    
    if opcion=='1':
        nombre=input('Nombre: ')
        if nombre not in telefonos:
            print('Ese nombre no existe...')
        else:
            telf=telefonos[nombre]
            print(nombre, ':', telf)
    elif opcion=='2':
        nombre=input('Nombre: ')
        if nombre in telefonos:
            print('Ese nombre ya está en la agenda...')
        else:
            telf=int(input('Telefono: '))
            telefonos[nombre]=telf
            print('el usuario se ah añadido correctamente...')
    elif opcion=='3':
        nombre=input('Nombre: ')
        if nombre not in telefonos:
            print('Ese nombre no está en la agenda...')
        else:
            telf=int(input('Telefono: '))
            telefonos[nombre]=telf
            print('El telefono se ah modificado correctamente...')
    elif opcion=='4':
        nombre=input('Nombre: ')
        if nombre not in telefonos:
            print('Ese nombre no está en la agenda...')
        else:
            del telefonos[nombre]
            print('el usuario se ah eliminado correctamente...')
    elif opcion=='5':
        consultando=False