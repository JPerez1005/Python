"""Escribir un programa que muestre la sumatoria 
de todos los múltiplos de 3 encontrados entre el
0 y el 100."""

cont=0
sum=0
for i in range(0,101):
    if i%3==0:
        cont=cont+1
        sum=sum+i

print('La cantidad de numeros encontrados multiplos de 3 es: ',cont)
print('Sumatoria de los múltiplos de 3:',sum)