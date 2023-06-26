"""Programa tablas de multiplicar
del 2 al 7"""

for i in range(1,11):
    for j in range(2,8):
        print('{:3} x{:2} ={:2}'.format(j,i,j*i), end='')
    print()