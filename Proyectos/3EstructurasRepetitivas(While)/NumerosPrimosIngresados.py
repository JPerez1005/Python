'''Escribir un programa que solicite el ingreso
de una cantidad indeterminada de números mayores
que 1, finalizando cuando se reciba un cero.
Imprimir la cantidad de números primos ingresados.
'''
Primo=0
i=2
while True:
    n=int(input('Digite un numero: '))
    if n>0:
        if n%i==0:
            Primo+=1
            print('Es primo')
    elif n<0:
        print('No se admiten numeros menores a cero')
    else:
        print('Saliendo')
        break
    i+=1

print(f'Numeros primos digitados: {Primo}')