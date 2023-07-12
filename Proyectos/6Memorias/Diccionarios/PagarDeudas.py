'''Programa que gestiona el pago de deudas'''

deudas={
    'Jorge':12,
    'Isabel':20,
    'Ana': 10,
    'Miguel': 8,
    'sara' : 15
}

def SaldarDeuda():
    nombre=input('Digite el nombre: ')
    validacion=deudas.pop(nombre,'No está registrado..')

def VerEntradas():
    pass

def VerTotalDeudas():
    print('-'*40)
    deudas_ord = sorted(deudas.keys())#Ordenamos
    for deuda in deudas_ord:#Recorremos dictionario
        print()
        print(f'{deuda}: {deudas[deuda]}')
        print()
    print('-'*40)
    return

while True:
    print('1.) Saldar Deuda.')
    print('2.) Ver Entradas.')
    print('3.) Ver el Total de Deudas.')
    print('4.) Salir...')
    try:
        opcion=int(input('Digite una opción: '))
        if opcion==1:
            SaldarDeuda()
        elif opcion==2:
            VerEntradas()
        elif opcion==3:
            VerTotalDeudas()
        elif opcion==4:
            print('Saliendo...')
            break
        else:
            print('Opción no valida')
    except ValueError:
        print('Digite valores validos')