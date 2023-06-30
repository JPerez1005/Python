'''Escribir una función que calcule el total
de una factura tras aplicarle el IVA. La función
debe recibir la cantidad sin IVA y el porcentaje
de IVA a aplicar, y devolver el total de la
factura. Si se invoca la función sin pasarle
el porcentaje de IVA, deberá aplicar un 21%.'''

def CalcularIva():
    ValorSinIVA=int(input('Digite el Valor sin IVA: '))
    ValorIVA=float(input('Digite el valor del porcentaje del iva: '))
    if ValorIVA=='':
        ValorIVA=21
    PorcentajeIVA=ValorIVA/100
    ValorTotal=PorcentajeIVA*ValorSinIVA
    print('\n','-'*5,'FACTURA','-'*5,'\n')
    print('El valor total de la factura es: ',ValorTotal)
    print('\n','-'*5,'Fin','-'*5,'\n')
