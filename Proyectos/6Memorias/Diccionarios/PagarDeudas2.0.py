'''Programa que gestiona el pago de deudas'''

deudas={
    'Jorge':12,
    'Isabel':20,
    'Ana': 10,
    'Miguel': 8,
    'sara' : 15
}

total=sum(list(deudas.values()))

while True:
    print()
    print('1.) Saldar Deuda.')
    print('2.) Ver Entradas.')
    print('3.) Ver el Total de Deudas.')
    print('4.) Salir...')
    print()
    
    opcion=''
    while opcion not in ('1','2','3','4'):
        opcion =input('->')
    
    if opcion=='1':
        nombre=input('Nombre a saldar: ')#pide nombre
        if nombre not in deudas:#si nombre no está en deudas
            print(f'No hay deudas para {nombre}')
        else:
            saldado=deudas.pop(nombre)#eliminamos el nombre
            #de la lista
            total-=saldado#a la suma total le quitamos lo que
            #debia ese nombre
            print('Deuda saldada: {}'.format(saldado))
    elif opcion=='2':
        for nombre,deuda in deudas.items():
            print('{:8}: {:4d}'.format(nombre, deuda))
    elif opcion=='3':
        print('Deuda Total: {}'.format(total))
    elif opcion=='4':
        break
    else:
        print('opcion no valida')