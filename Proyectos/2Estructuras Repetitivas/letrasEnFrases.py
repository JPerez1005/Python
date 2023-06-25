"""Escribir un programa en el que se pregunte 
al usuario por una frase y una letra, y
 muestre por pantalla el número de veces 
 que aparece la letra en la frase.
"""

Frase=input('Digite una frase: ')
Letra=input('Digite una letra: ')
cont=0
for letra in Frase:
    if letra==Letra:
        cont=cont+1
    
print(f'La letra {Letra} en esa frase se encuentra {cont} veces')