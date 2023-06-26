"""Programa que muestra las letras de una palabra
a excepcion de la letra que digite el usuario"""

Palabra=input('Digite una palabra: ')
Letra=input('Digite una letra: ')

for Letras in Palabra:
    if Letras==Letra:
        continue
    elif Letras!=Letra:
        print(Letras, end='')