"""De una serie de números ingresados por el usuario, 
imprima cuales de estos son primos y cuáles no.
El ingreso de los números se termina cuando el usuario 
ingrese un numero negativo."""


i=2
INF=float('inf')
while i<INF:
    i=2
    primo=True
    culpable=0
    n=int(input('digitar un numero: '))
    if n<0:
        print('Saliendo....')
        break
    if n%i==0:
        primo=False
        culpable=i
    i=i+1

    if primo>0:
        print('El numero es primo')
    else:
        print('El numero no es primo ',culpable)