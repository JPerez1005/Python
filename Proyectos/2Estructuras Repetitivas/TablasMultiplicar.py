"""Realizar un programa que solicite la 
carga de un valor entero del 1 al 10. 
Mostrar después la tabla de multiplicar 
de dicho número."""

Num=int(input('Digite un numero del uno al diez: '))

for i in range(1,11):
    print(f'{Num} x {i}= {Num*i}')
