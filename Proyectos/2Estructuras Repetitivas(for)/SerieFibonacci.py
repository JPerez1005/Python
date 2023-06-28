"""Crear un algoritmo que muestre los primeros
10 números de la sucesión de Fibonacci. La 
sucesión comienza con los números 0 y 1 y, 
a partir de éstos, cada elemento es la suma 
de los dos números anteriores en la secuencia: 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…"""
n1=0
n2=1
print(n1, end=', ')
print(n2, end=', ')
while True:
    try:
        num=int(input('digite un numero: '))
        for i in range(num):
            n3=n1+n2
            print(n3, end=', ')
            n1=n2
            n2=n3
        break
    except ValueError:
        print('Digite un numero valido')
