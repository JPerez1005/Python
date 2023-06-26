"""Escribir un programa que pida al usuario
un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo,
de altura el número introducido."""

#piramide de asteriscos
#otra forma de uso del rango

a='*'
Num=int(input('Digite un numero: '))
for numero in range(1,Num+1):#inicia en cero, termina en 9 y aumenta en 2
    print('salida=',numero,numero*a)