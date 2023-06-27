"""De una serie de números ingresados por el usuario, indique
 cual es el menor y el mayor de estos.
El ingreso de los números se termina cuando 
el usuario ingrese un numero negativo."""

n=int(input('Ingrese cuantos numeros va a digitar: '))
nMayor=0
nMenor=float('inf')
i=1
while i<=n:
    num=int(input('Digite un numero: '))
    if num>nMayor:
        nMayor=num
    if num<nMenor:
        nMenor=num
    if num<0:
        print('saliendo...')
        break
    i=i+1

print(f'El numero mayor es: {nMayor}')
print(f'El numero menor es: {nMenor}')
