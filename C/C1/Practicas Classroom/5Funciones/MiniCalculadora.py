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
        print('1.) Sumar')
        print('2.) Restar')
        print('3.) Multiplicar')
        print('4.) Dividir')
        print('5.) Potencia')
        print('6.) Factorial')
        print('7.) Salir...')
        op=LeerInt('\n>> Opción (1 a 7): ')
        if op<1 or op>7:
            msgError('Opcion no valida')
            continue
        return op


def Sumar():
    print('\n'*3, '*** 1. SUMAR ***')
    N1=LeerInt('Ingrese un numero: ')
    N2=LeerInt('Ingrese otro numero: ')
    print('\nEl resultado de la suma es: ',N1+N2)
    input('\nPresione cualquier tecla para volver al menu...')

def Restar():
    print('\n'*3, '*** 2. RESTAR ***')
    N1=LeerInt('Ingrese un numero: ')
    N2=LeerInt('Ingrese otro numero: ')
    print('\nEl resultado de la resta es: ',N1-N2)
    input('\nPresione cualquier tecla para volver al menu...')

def Multiplicar():
    print('\n'*3, '*** 3. MULTIPLICAR ***')
    N1=LeerInt('Ingrese un numero: ')
    N2=LeerInt('Ingrese otro numero: ')
    print('\nEl resultado de la multiplicación es: ',N1*N2)
    input('\nPresione cualquier tecla para volver al menu...')

def Dividir():
    print('\n'*3, '*** 4. DIVIDIR ***')
    N1=LeerInt('Ingrese un numero: ')
    N2=LeerInt('Ingrese otro numero: ')
    while N2==0:
        print('ingrese un numero diferente de cero')
        N2=LeerInt('Ingrese otro numero: ')
    print('\nEl resultado de la dividición es: ',round(N1/N2, 2))
    input('\nPresione cualquier tecla para volver al menu...')

def Potencia():
    print('\n'*3, '*** 5. POTENCIA ***')
    N1=LeerInt('Ingrese un numero: ')
    N2=LeerInt('Ingrese otro numero: ')
    print('\nEl resultado de la Potencia es: ',N1**N2)
    input('\nPresione cualquier tecla para volver al menu...')

def Factorial():
    print('\n'*3, '*** 6. Factorial ***')
    N1=LeerInt('Ingrese un numero: ')
    F=1
    for i in range(1, N1+1):
        F*=i
    print('\nEl Resultado del factorial es: ',F)
    input('Presione cualquier tecla para volver al Menu...')





#PROGRAMA GENERAL
while True:
    opcion=Menu()

    if opcion==1:
        Sumar()
    elif opcion==2:
        Restar()
    elif opcion==3:
        Multiplicar()
    elif opcion==4:
        Dividir()
    elif opcion==5:
        Potencia()
    elif opcion==6:
        Factorial()
    elif opcion==7:
        print('\n**Gracias por usar la mini calculadora**\n')
        break
    else:
        msgError('Opcion Invalida.')