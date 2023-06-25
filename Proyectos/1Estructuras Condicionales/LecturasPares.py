"""Leer un string y mostrar "True" si la cantidad
de caracteres es un numero par, o 'False' es impar"""

Texto=input('Ingrese una frase: ')
Longitud=len(Texto)
if Longitud % 2 == 0:
    print('True')
    print('Es par')
else:
    print('False')
    print('Es impar')