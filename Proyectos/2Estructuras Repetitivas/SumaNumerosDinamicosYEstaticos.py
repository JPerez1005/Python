"""Programa que pide un numero al usuario. 
Si ese numero más algún numero de la lista
dada es igual a 100, el programa dice que
el numero cumple con la condición"""

Lista=[28,36,43,52,61,75,84,97]

Num=int(input('Digite un numero: '))

for elements in Lista:
    if (elements+Num)==100:
        print(f'El numero: {Num}')
        print(f'y el numero de la lista: {elements}')
        print('Cumplen con la condicion de ser un total de ',elements+Num)
    else:
        print('El numero no cumple')