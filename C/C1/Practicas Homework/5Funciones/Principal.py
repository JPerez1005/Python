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
        print('1.) Cantidad de palabras en un String')
        print('2.) Calcular el mcd de dos números')
        print('3.) Calcular el IVA de una factura')
        print('4.) Salir...')
        op=LeerInt('\n>> Opción (1 a 4): ')
        if op<1 or op>4:
            msgError('Opcion no valida')
            continue
        return op

def NumeroDePalabras():
    Oracion=input('Digite una oracion: ')

    if Oracion.isdigit():
        while True:
            print('No se admiten numeros...')
            Oracion=input('Digite una oracion: ')
            if not Oracion.isdigit():
                break

    espacios=Oracion.split(' ')
    print(len(espacios))



def MCD():
    B=True
    while B:

        num1=input('digite un numero: ')
        num2=input('digite otro numero: ')
        if num1.isdigit() and num2.isdigit:
            if num2!='0' and num1!='0':
                B=False
            else:
                print('Tiene que ser diferente de cero')
        else:
            print('No puede digitar letras..')

    num1=int(num1)
    num2=int(num2)
    if num2>num1 :
        reserva=num2
        num2=num1
        num1=reserva
    res=1
    while res!=0:
        cociente=num1//num2
        res=num1%num2
        num1=num2
        num2=res
    
    print('el maximo comun divisor es: ',num1)

    print('fin')

def CalcularIva():
    ValorSinIVA=int(input('Digite el Valor sin IVA: '))
    ValorIVA=input('Digite el valor del porcentaje del iva: ')

    if ValorIVA=='':
        ValorIVA=21
    ValorIVA=float(ValorIVA)
    PorcentajeIVA=ValorIVA/100
    ValorTotal=PorcentajeIVA*ValorSinIVA
    print('\n','-'*5,'FACTURA','-'*5,'\n')
    print('El valor del producto es: ',ValorSinIVA)
    print('El prorcentaje del IVA es: ',ValorIVA)
    print('El valor del IVA es: ',ValorTotal)
    print('El valor total de la factura es: ',ValorSinIVA+ValorTotal)
    print('\n','-'*5,'Fin','-'*5,'\n')

#PROGRAMA GENERAL
while True:
    opcion=Menu()

    if opcion==1:
        NumeroDePalabras()
    elif opcion==2:
        MCD()
    elif opcion==3:
        CalcularIva()
    elif opcion==4:
        print('\n**Gracias por usar este MiniProgramaMultiProcesos**\n')
        break
    else:
        msgError('Opcion Invalida.')