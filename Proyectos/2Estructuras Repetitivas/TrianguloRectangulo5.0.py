"""Triangulo de numeros"""

for i in range(5,0,-1):
    cont=6
    if i<5:
        cont=i+1
    for j in range(i,0,-1):
        cont=cont-1
        print(cont, end='')
    print('')