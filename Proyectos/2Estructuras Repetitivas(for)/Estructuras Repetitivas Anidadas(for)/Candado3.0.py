"""Programa que adivina una clave mediante fuerza bruta.
La clave consiste en 4 letras minusculas"""

from time import time

Clave=input('Dime una clave: ')
Alfabeto='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'

inicio=time()

for c1 in Alfabeto:
    for c2 in Alfabeto:
        for c3 in Alfabeto:
            for c4 in Alfabeto:
                for c5 in Alfabeto:
                    Intento=c1+c2+c3+c4+c5
                    if Intento == Clave:
                        print('Clave Encontrada: ', Intento)

final=time()
res = final-inicio
print(f"La clave tardó: {round(res,5)} segundos en encontrarse")