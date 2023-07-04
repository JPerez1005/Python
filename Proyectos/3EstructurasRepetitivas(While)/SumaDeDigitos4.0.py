'''Crear un programa que solicite el ingreso de
números enteros positivos, hasta que el usuario
ingrese el 0. Por cada número, informar cuántos
dígitos pares y cuántos impares tiene.

Al finalizar, informar la cantidad de dígitos
pares y de dígitos impares leídos en total.'''
pares=0
impares=0
n=1
suma=0
while True:
    n=int(input('Digite un numero: '))
    if n==0:
        break
    if n%2 == 0:
        pares+=1
    else:
        impares+=1
    suma=0
    while n!=0:
        digito=n%10
        suma+=digito
        n=n//10
    print("Suma de sus dígitos:", suma)

print(f'Hubo un total de {pares} numeros pares...')
print(f'Hubo un total de {impares} numeros impares...')