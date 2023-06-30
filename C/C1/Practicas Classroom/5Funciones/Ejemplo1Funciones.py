#SINTAXIS GENERAL
"""def NombreFunction([param1,param2,param3]):
    CuerpoFunction"""

def LeerInt(msg):
    while True:
        try:
            n=int(input(msg))
            return n#Se sale de todo
        except ValueError:
            print('Error!. Ingrese un numero entero valido.')

'''Suma de numeros'''

def Sum(N1,N2):
    S=N1+N2
    return S

a=LeerInt('Ingrese un numero: ')
b=LeerInt('Ingrese otro numero: ')

print('El Resultado es ',Sum(a,b))