'''Programa que pide un numero de inicio
y otro final al usuario, y que suma todos
los numeros multiplos de 3 que hay entre
ellos.'''

Inicio=int(input('Digite un numero de inicio: '))
Final=int(input('Digite un numero de final: '))
Inicio1=Inicio
Suma=0
while Inicio<=Final:
    if Inicio%3==0:
        Suma=Suma+Inicio
    Inicio+=1

print(f'La suma de todos lo numeros entre: \
      {Inicio1} y {Final}')
print(f'es: {Suma}')