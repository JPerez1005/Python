'''Se tiene una lista de vendedores de una empresa, sobre las ventas realizadas en
el mes. La información que se conoce de cada vendedores la siguiente:

•Cédula de ciudadanía
•Nombre
•Tipo de vendedor, que puede ser

    o1:Puerta a Puerta
    o2:Telemercadeo
    o3:Ejecutivo de ventas
oValor ventas realizadas en el mes

NOTA:La lista termina cuando la cédula de ciudadanía es -1

También nos suministran el porcentaje de comisión que se le aplica a las ventas 
realizadas en el mes, para el cálculo de la comisión, de acuerdo al tipo de 
vendedor así:

•Si el vendedor es puerta a puerta, el porcentaje de comisión es del 20% sobre el 
valor de las ventas realizadas en el mes.
•Si el vendedor es telemercadeo, el porcentaje de comisión es del 15% sobre el 
valor de las ventas realizadas en el mes.
•Si el vendedor es ejecutivo de ventas, el porcentaje de comisión es del 25% sobre 
el valor de las ventas realizadas en el mes.

Se pide calcular el valor a pagar por comisión  de cada vendedor, el valor total 
de la ventas del mes, el valor total a pagar por comisiones.
'''

def TipoVendedor(ValorVenta,Desicion):
    
    if Desicion==1:
        Porcentaje=0.2
        Comision=ValorVenta*Porcentaje
    elif Desicion==2:
        Porcentaje=0.15
        Comision=ValorVenta+Porcentaje
    elif Desicion==3:
        Porcentaje=0.25
        Comision=ValorVenta+Porcentaje
    
    return Porcentaje, Comision


while True:
    try:
        Cedula=int(input('Ingrese el numero de su cedula de ciudadania: '))
        if Cedula==-1:
            break
        Nombre=input('Ingrese su nombre: ')
        ValorVenta=int(input('Digite el valor de la venta: '))
        print('Tipos de Vendedores:\n')
        print('1.)Puerta a Puerta')
        print('2.)Telemercadeo')
        print('3.)Ejecutivo de Ventas\n')
        Desicion=int(input('Digite el numero del tipo de vendedor: '))
        if 0>Desicion>3:
            print('No se encontró la opción...')
            continue#Lo reinicia
        rPorcentaje,rComsion=TipoVendedor(ValorVenta,Desicion)
        
        print(f'El resultado de la comisión es: {rComsion}')
        print(f'Tiene un porcentaje de {rPorcentaje}')
    except ValueError:
        print('No puede ingresar letras')


