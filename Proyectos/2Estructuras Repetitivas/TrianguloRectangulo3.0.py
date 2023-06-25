"""Escribir un programa que pida al usuario un número
entero y muestre por pantalla un triángulo rectángulo
como el de más abajo."""

Num=int(input('Digite un numero entero: '))

for i in range(Num):#i llega hasta cinco
    for j in range(i+1):
        #print(i+1 , end=' ')#esto nos imprime un triangulo de uno a Num siendo uno la cima
        # print(j+1 , end=' ')#Esto nos imprime todo el uno a la izquierda
        print(j, end=' ')
    print(' ')