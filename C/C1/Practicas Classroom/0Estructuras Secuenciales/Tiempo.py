"""Dado una cantidad de segundo, indique cuantas horas, minutos y segundos corresponde.
entrada 1:
segundos=125
salida=1
hora=0
minutos=2
segundos=5

entrada 2:
segundos=3725
salida=2
hora=1
minutos=2
segundos=5
"""

segundos=int(input('Ingrese la cantidad de segundos: '))
Horas=segundos//3600
minutos=(segundos//60)%60
Seconds=segundos%60
print(f'Horas= {Horas}')
print(f'Minutos= {minutos}')
print(f'segundos= {Seconds}')