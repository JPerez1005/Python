"""Construya un programa que me ayude a encontrar el próximo número de la siguiente serie.
1, 1, 2, -1, 1, -2, ?
"""
cont=1
for i in range(1,-2,-2):
    for j in range(1,-2,-2):
        if i<0 and j<0:
            print(f'{j}, {i}, ', end=' ')
            i=1
            j=1
            print(f'{i+j}', end='.')
        elif i<0 or j<0:
            if j<0:
                print(f'{j}, {i}, {j-i}', end=', ')
            else:
                print(f'{j}, {i}, {-j+i}', end=', ')
        else:
            print(f'{j}, {i}, {j+i}', end=',')
