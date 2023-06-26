"""Programa que muestra todas las posibles combinaciones
para poder abrir un candado de clave de tres ruedas"""
import random
numero=str(random.randint(0,1000))
numero2=str(random.randint(0,1000))
numero3=str(random.randint(0,1000))
n1=0
n2=0
n3=0
for x in range(0,10):
    for y in range(0,10):
        for z in range(0,10):
            xyz=f'{x}{y}{z}'
            if xyz==numero:
                n1=xyz
                print(f'El primer numero es: {xyz}')
for x in range(0,10):
    for y in range(0,10):
        for z in range(0,10):
            xyz=f'{x}{y}{z}'
            if xyz==numero2:
                n2=xyz
                print(f'El segundo numero es: {xyz}')
for x in range(0,10):
    for y in range(0,10):
        for z in range(0,10):
            xyz=f'{x}{y}{z}'
            if xyz==numero3:
                n3=xyz
                print(f'El tercer numero es: {xyz}')

print('El resutado de la clave es: {:1} {:1} {:1}'.format(n1,n2,n3))