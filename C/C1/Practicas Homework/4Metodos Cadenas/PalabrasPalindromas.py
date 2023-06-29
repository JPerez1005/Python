"""Hacer un prgrama que reciba una palabra e indicar si esta
es palindroma o no

una palabra palindroma es aquella que se lee igual
adelante que atras"""

salida=0

while salida==0:
    palabra=input('Digite una palabra: ')
    cant=len(palabra)
    es_palindromo=True

    for i in range(cant//2):#iterar hasta la mitad de la palabra
        if palabra[i] != palabra[cant -1 -i]:
            es_palindromo=False
            break

    if es_palindromo:
        print('la palabra es palindroma')
    else:
        print('la palabra no es palindroma')
    
    salida=int(input('para terminar digite un numero diferente de cero: '))
    

print('fin')