"""Requerir al usuario que ingrese un número entero
positivo e imprimir todos los números correlativos
entre el ingresado por el usuario y uno menos del
doble del mismo."""

Num=int(input('Ingrese un Numero: '))

Doble=(Num*2)

for i in range(Num, Doble):
    print(i, end=', ')