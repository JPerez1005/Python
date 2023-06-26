"""Solicitar al usuario que ingrese una frase 
y luego imprimir la cantidad de vocales que se 
encuentran en dicha frase."""

frase=input('Ingrese una frase: ')
cont=0
for x in 'aeiou':
    if x in frase:
        cont=cont+1

print(f'\nHay un total de {cont} vocales en esa frase')