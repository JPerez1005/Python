'''Solicitar al usuario que ingrese números enteros
positivos y, por cada uno, imprimir la suma de los
dígitos que lo componen. La condición de corte es
que se ingrese el número -1. Al finalizar, mostrar
cuántos de los números ingresados por el usuario
fueron números pares.'''
par=0
n=1
while n>-1:
    n=int(input('Ingrese un numero positivo: '))
    Suma=0
    if n%2==0:
        par=par+1
    while n!=0 and n>-1:
        Digitos=n%10
        Suma=Suma+Digitos
        n=n//10
    print(f'La suma del numero digitado es: {Suma}')
    
print(f'Hubo un total de {par} numeros pares...')