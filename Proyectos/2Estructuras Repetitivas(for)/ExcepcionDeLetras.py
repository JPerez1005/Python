"""Programa que muestra las letras de una palabra
a excepcion de la letra que digite el usuario"""

Frase=input('Digite alguna frase o palabra: ')
Letra=input('Alguna letra que quiera omitir?: ')

for Letras in Frase:
    if Letras==Letra:
        print('', end='')
    elif Letras!=Letra:
        print(Letras, end='')