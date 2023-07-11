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
    print('1.) Consultar por nombre')
    print('2.) Consultar por telefono')
    print('3.) Listar la agenda')
    print('4.) Salir')
    print('\n','-'*40,'\n')

    opcion=''
    while opcion not in ('1','2','3','4','5'):
        opcion=input('-> ')
    
    if opcion=='1':
        nombre=input('Nombre: ')
        telf=telefonos.get(nombre, 'Ese nombre no existe.')
        print('{}: {}'.format(nombre,telf))
    elif opcion=='2':
        telf_buscado = int(input('Telefono: '))
        if telf_buscado in telefonos.values():
            for nombre,telf in telefonos.items():#recorremos toda la lista
                if telf_buscado==telf:
                    print('{}: {}'.format(telf,nombre))
        else:
            print('ese telefono no está en la agenda...')
    elif opcion=='3':
        for nombre, telf in telefonos.items():
            print('{}: {}'.format(nombre, telf))
    elif opcion=='4':
        consultando=False
            
