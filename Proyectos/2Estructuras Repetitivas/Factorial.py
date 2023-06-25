"""Dado un número entero positivo, mostrar 
su factorial. El factorial de un número se 
obtiene multiplicando todos los números 
enteros positivos que hay entre el 1 y ese número."""

Num=int(input('Digite un numero: '))
fact=1
for i in range(1,Num+1):
    fact=fact*i
print(fact)