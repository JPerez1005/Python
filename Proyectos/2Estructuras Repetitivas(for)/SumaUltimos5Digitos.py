"""Desarrollar un programa que solicite la carga 
de 10 números e imprima la suma de los últimos 5 
valores ingresados."""

suma=0

for i in range(11):
    num=int(input('Digite un numero:'))
    if i>5:
        suma=suma+num

print(f'La suma de los ultimos 5 digitos es: {suma}')