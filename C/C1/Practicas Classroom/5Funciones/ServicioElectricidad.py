'''Dado el nombre y estrato(1,2,3,4,5) de un usuario del servicio
deenergía eléctrica, calcularlo que pagaría de tarifa básicadel
servicio de energía eléctrica , que depende del estrato,así
Estrato Tarifa Básica
1$10.000
2$15.000
3$30.000
4$50.000
5$65.000
Se pide visualizar el nombre y tarifa básica'''

#Funciones
def LeerInt(msg):
    while True:
        try:
            n=int(input(msg))
            if n<1 or n>5:
                print('Error!! Ingrese un estrato valido...')
                input('digite cualquier tecla para continuar....')
                continue#Para que vuelva y pregunte
            return n#Se sale de todo
        except ValueError:#Para solo numeros
            print('Error!. Ingrese un numero entero valido.')

def LeerString(msg):
    while True:
        try:
            n=(input(msg))
            if n.strip()=='':#que el usuario no digite un valor vacío
                print('Error!! Ingrese un nombre valido...')
                input('digite cualquier tecla para continuar....')
                continue#Para que vuelva y pregunte
            return n#Se sale de todo
        except ValueError as e:
            print('Error!. Ingrese un numero entero valido.', e.message)#nos retorna el error

def CalTarifaBasica(estrato):#el parametro se puede llamar como quiera
    if estrato==1:
        return 10000#return lo saca de todo
    elif estrato==2:
        return 15000
    elif estrato==3:
        return 30000
    elif estrato==4:
        return 50000
    else:
        return 65000
    
##PROGRAMA GENERAL
nombre=LeerString('Ingrese un nombre:  ')
estrato=LeerInt('Ingrese el estrato del usuario: ')

TarifaBas=CalTarifaBasica(estrato)

print('Nombre del usuario: ', nombre)
print('Tarifa Basica del usuario: ', TarifaBas)
