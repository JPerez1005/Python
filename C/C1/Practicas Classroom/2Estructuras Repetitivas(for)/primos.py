"""Determinar si un numero es primo o no"""

n=int(input('digitar un numero: '))

primo=True
culpable=0
for i in range(2,n):
    if n%i==0:
        primo=False
        culpable=i

if primo:
    print('El numero es primo')
else:
    print('El numero no es primo ',culpable)