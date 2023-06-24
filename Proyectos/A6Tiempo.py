"""Construir un programa que , dado un numero total de
horas , devuelve el numero de semanas, dias y horas equivalentes.
Por ejemplo, dado un total de 1000 horas debe mostrar 5 semanas, 6 dias 
y 16 horas"""

HorasTotales=int(input('Digite el numero de horas: '))

Semanas = HorasTotales//168
Dias = HorasTotales%168//24
Horas = HorasTotales%24

print(f'El quivalente es: \nSemanas:{Semanas}\nDias: {Dias}\nHoras: {Horas}')
