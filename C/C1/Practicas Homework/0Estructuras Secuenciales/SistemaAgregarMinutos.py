Hora = int(input('Digite la hora: '))
Minutos=int(input('Digite los minutos: '))

print(f'Hora actual: {Hora} : {Minutos}')
Minutosagregados=int(input('Digite cuantos minutos quiere agregar: '))
MinutosTotales= (Hora*60) + Minutos+Minutosagregados
Hora=MinutosTotales//60
Minutos = MinutosTotales-(Hora*60)
if Hora>=24:
    Minutos = MinutosTotales-(Hora*60)
    Hora=0
print('------------------RESULTADO-------------------\n')
print(f'Nueva hora: {Hora} : {Minutos}\n')