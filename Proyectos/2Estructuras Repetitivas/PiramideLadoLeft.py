"""Imprima el siguiente patrón con el ciclo for:
Es una piramide de lado
"""

for i in range(1, 6):
    for j in range(1, i):
        print('*', end=' ')
    print('')

for x in range(6, 1,-1):
    for y in range(x, 1,-1):
        print('*', end=' ')
    print('')