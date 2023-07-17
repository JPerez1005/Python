"""Búsqueda de palabra clave: Escribe un programa que solicite al usuario que ingrese una oración y una
palabra clave específica. El programa debe verificar si la palabra clave está presente en la oración y
mostrar un mensaje apropiado. Si la palabra clave se encuentra, el programa debe detenerse y mostrar
un mensaje de éxito. Si la palabra clave no se encuentra en la oración, el programa debe continuar
pidiendo al usuario que ingrese otra oración hasta que se encuentre la palabra clave o el usuario ingrese
"salir" para terminar el programa."""

while True:
    Oracion=input('Escriba una oración: ')
    Palabra=input('Digite una palabra: ')
    if Palabra.isalpha():
        if Oracion.find(Palabra):
            print(' si está')
            break
        elif Oracion!=Palabra:
            print(' No está')
        elif 'salir'==Palabra.lower():
            break
    else:
        print('No digite numeros!!')