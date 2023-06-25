"""Escribir un programa que permita al usuario ingresar dos años 
y luego imprima todos los años en ese rango, que sean bisiestos 
y múltiplos de 10. Nota: para que un año sea bisiesto debe 
ser divisible por 4 y no debe ser divisible por 100, excepto 
que también sea divisible por 400."""

Anio=int(input('Ingrese un año inicial: '))
Anio2=int(input('Ingrese un año final: '))
cont=0
for i in range(Anio,Anio2):
    if i%4==0 and (i%100!=0 or i%400==0):
        cont=cont+1
        print(i,' Año bisiesto')
    elif i%10==0:
        cont=cont+1
        print(i, 'Multiplo de 10')

if cont==0:
    print('\nNingun año cumplió con las condiciones')
    print('No eran ni bisiestos ni multiplos de 10\n')