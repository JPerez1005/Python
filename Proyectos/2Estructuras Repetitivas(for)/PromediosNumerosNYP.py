"""Escribir un programa que permita al 
usuario ingresar 6 números enteros, 
que pueden ser positivos o negativos. 
Al finalizar, mostrar la sumatoria de 
los números negativos y el promedio de los positivos.
No olvides que no es posible dividir por
cero, por lo que es necesario evitar que 
el programa arroje un error si no se 
ingresaron números positivos."""

CantNum=int(input('Ingrese la cantidad de numeros a digitar: '))
cont=0
NumP=0
NumN=0
for i in range(1,CantNum+1):
    cont=cont+1
    Num=float(input(f'{i}.) Digite el numero: '))
    if Num>0:
        NumP=NumP+Num
    elif Num<0:
        NumN=NumN+Num
    else:
        print('Saliendo...')
        break

print(f'Sumatoria de numeros negativos: {NumN}')
print('Promedio de numeros positivos: {:.2f}'.format(NumP/cont))