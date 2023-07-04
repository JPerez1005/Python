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
        print('1.) Imprima los dos primeros caracteres.')
        print('2.) Imprima los tres últimos caracteres.')
        print('3.) Omitir caracteres de dos en dos.')
        print('4.) Invertir Frase.')
        print('5.) Frase Espejo.')
        print('6.) Interferir entre los caracteres.')
        print('7.) Remplazar caracteres.')
        print('8.) Ocultar Contraseña de numeros.')
        print('9.) Interferencia entre cadenas cada 3 caracteres.')
        print('10.) Saliendo...')
        op=LeerInt('\n>> Opción (1 a 10): ')
        if op<1 or op>11:
            msgError('Opcion no valida')
            continue
        return op
    
def DosPrimerosCaracteres():
    mensaje9 = input('Digite una cadena de caracteres: ')
    mensaje9a = mensaje9[0:2]
    print(mensaje9a)

def TresUltimosCaracteres():
    mensaje9 = input('Digite una cadena de caracteres: ')
    mensaje9a = mensaje9[len(mensaje9)-3:len(mensaje9)]
    print(mensaje9a)

def OmitirCaracteres():
    Cadena=input('Ingrese una frase: ')
    resultado = Cadena[::2]#se salta letras
    print(resultado)

def InvertirFrase():
    cadena = input('Digite una Frase: ')
    resultado = cadena[::-1]
    print(resultado)


def FraseEspejo():
    cadena = input('Digite una frase: ')
    resultado = cadena + cadena[::-1]
    print(resultado)


def InterferenciaDeCaracteres():
    cadena = input('Digite una frase: ')
    caracter = ","
    resultado = caracter.join(cadena)
    print(resultado)

def RemplazoDeCaracteres():
    cadena = input('Digite una frase: ')
    caracter = "_"
    resultado = cadena.replace(" ", caracter)
    print(resultado)

def OcultarContraseñaDeNumeros():
    cadena = input('Digite una contraseña: ')
    tabla_de_sustitucion = str.maketrans("0123456789", "x" * 10)
    resultado = cadena.translate(tabla_de_sustitucion)
    print(resultado)

def InterferenciaDeCaracteresDe3En3():
    cadena = "2552552550"
    caracter = "."
    segmentos = []

    for i in range(0, len(cadena), 3):
        segmento = cadena[i:i+3]
        segmentos.append(segmento)

    nueva_cadena = caracter.join(segmentos)
    print(nueva_cadena)



#PROGRAMA GENERAL
while True:
    opcion=Menu()

    if opcion==1:
        DosPrimerosCaracteres()
    elif opcion==2:
        TresUltimosCaracteres()
    elif opcion==3:
        OmitirCaracteres()
    elif opcion==4:
        InvertirFrase()
    elif opcion==5:
        FraseEspejo()
    elif opcion==6:
        InterferenciaDeCaracteres()
    elif opcion==7:
        RemplazoDeCaracteres()
    elif opcion==8:
        OcultarContraseñaDeNumeros()
    elif opcion==9:
        InterferenciaDeCaracteresDe3En3()
    elif opcion==10:
        print('\n**Gracias por usar las cadenas de caracteres**\n')
        break
    else:
        msgError('Opcion Invalida.')