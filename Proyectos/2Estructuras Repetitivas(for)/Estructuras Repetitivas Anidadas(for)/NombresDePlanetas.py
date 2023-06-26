"""Para un juego que va a tener 20000 planetas
necesitamos formar nombres para cada uno de ellos
. Crea una lista con todos los nombres de 3 sílabas
que se pueden formar con tres consonantes y cinco
vocales, de tal forma de tal forma que se intercambien
consonante y vocal, y no se repita ninguna letra 
en cada nombre. Al final muestra la cantidad de
nombres de la lista y muestra 10 al azar"""

import random

Consonantes='sdgfbnhkfglfdñ'
Vocales='aeiou'
Nombres=[]

for c1 in Consonantes:
    for v1 in Vocales:
        for c2 in Consonantes:
            for v2 in Vocales:
                for c3 in Consonantes:
                    for v3 in Vocales:
                        if c1!=c2 and c1!=c3 and c2!=c3 and \
                            v1!=v2 and v1!=v3 and v2!=v3:
                             Nombres=c1+v1+c2+v2+c3+v3
                             Nombres.append(Nombres)

print('')