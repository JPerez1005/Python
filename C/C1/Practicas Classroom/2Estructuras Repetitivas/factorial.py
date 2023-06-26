"""Hacer un programa que calcule el factorial de un numero"""

n=int(input('Digite un numero: '))

fact=1
for i in range(1,n+1):
    fact=fact*i
    print(f'El factorial del numero digitado {n} es: {fact}')

#print(f'El factorial del numero digitado {n} es: {fact}')

