"""Programa tablas de multiplicar
del 2 al 7"""

for t in range(2,8):
    for i in range(1,11):
        op=t*i
        print(f'{t} x {i} = {op}')