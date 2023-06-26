"""Programa que comprueba si un elemento está en una
list y nos dice en qué posición (índice) se encuentra"""

Lista= [2,5,90,23,45,87,54,11,38]

Num=int(input('Digite un numero: '))

cont2=0
for Elemento in Lista:
    # print(pos)
    cont2+=1
    if Elemento==Num:
        print('Si se encuentra y está en la posicion: ',cont2)
    # print(Elemento)
