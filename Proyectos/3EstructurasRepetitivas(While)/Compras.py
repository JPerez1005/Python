'''Crear un programa que permita al usuario
ingresar los montos de las compras de un cliente
(se desconoce la cantidad de datos que cargará,
la cual puede cambiar en cada ejecución),
cortando el ingreso de datos cuando el usuario
ingrese el monto 0.

Si ingresa un monto negativo, no se debe procesar
y se debe pedir que ingrese un nuevo monto.
Al finalizar, informar el total a pagar teniendo
que cuenta que, si las ventas superan el total
de $1000, se le debe aplicar un 10% de descuento.
'''
Suma=0
while True:
    Monto=int(input('Ingrese el monto: '))
    if Monto>0:
        Suma=Suma+Monto
    elif Monto==0:
        print('Saliendo...')
        break
    else:
        print('Monto no Valido...')

if Suma>1000:
    Descuento=Suma*0.1
    Suma=Suma-Descuento
    print('Se hizo un descuento del 10%\n')
    print(f'Se descontará un total del {Descuento}')

print(f'Total a pagar: {Suma}')
