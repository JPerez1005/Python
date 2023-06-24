#a.	Leer un número entero  y determine  si el  número es primo o no

salida=0

while salida==0:
    numero=input('digite un numero: ')
    numero=int(numero)
    if numero%2==0:
        print('el numero es par')
    else :
        print('el numero es impar')

    salida=input('para salir digite un numero diferente de cero, si no es así digite cero: ')
    salida=int(salida)

print('fin')