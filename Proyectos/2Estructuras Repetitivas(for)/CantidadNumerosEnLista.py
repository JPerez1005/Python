"""Programa que comprueba cuántas veces está
un numero en una lista dada:"""

Lista=[28,36,43,52,61,43,75,84,43,97]
cont=0
Num=int(input('Digite un numero de uno a cien: '))

for elements in Lista:
    if elements==Num:
        cont=cont+1

if cont>0:
    print(f'El numero {Num} si se encuentra')
    print(f'y se repite {cont} veces')
else:
    print('El numero no se encuentra en la lista')