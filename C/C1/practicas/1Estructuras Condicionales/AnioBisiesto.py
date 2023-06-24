"""Escribe un programa en Python que determine si un 
año ingresado por el usuario es bisiesto o no. Un
año bisiesto es aquel que es divisible entre 4, 
excepto aquellos divisibles entre 100 pero no entre 400.
El programa debe realizar lo siguiente:
Solicitar al usuario que ingrese un año.
Verificar si el año cumple con las condiciones para ser bisiesto.
Mostrar un mensaje indicando si el año es bisiesto o no."""

Anio=int(input('Digite un año: '))
Cociente=Anio/4

print('-'*10, 'Resultado','-'*10,'\n')

if Anio%4==0:
    print('Es bisiesto')
elif Anio%100==0:
    if Anio%400==0:
        print('Es bisiesto')
    else:
        print('No es bisiesto')
else:
    print('No es bisiesto')

print('-'*10, 'Fin','-'*10,'\n')