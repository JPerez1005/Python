'''Programa que suma los numeros pares
que hay entre el 1 y el 20'''

cont=0
suma=0
while cont<20:
    cont+=1
    if cont%2==0:
        suma=suma+cont

print('La suma de los numeros pares es: ',suma)