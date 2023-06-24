"""Hacer un algoritmo que, dada una hora con minutos y minutos adicionales, calcule la nueva hora.
Asuma que no se pasa de las 23:59
Ejemplo
Hora: 10:45
Minutos: 20
Nueva Hora: 11:05
"""

HoraOld=int(input('Digite la hora en la que está: '))
MinutosOld=int(input('Digite los minutos de la hora: '))

MinutosAgregados=int(input('Digite los minutos que quiere agregar: '))

Hora=MinutosAgregados//60
Minutos=MinutosAgregados%60

HoraNew=HoraOld+Hora
MinutosNew=MinutosOld+Minutos

while MinutosNew >= 60:
    MinutosNew -= 60
    HoraNew += 1
    while MinutosNew >= 120:
        MinutosNew -= 120
        HoraNew += 1
        while MinutosNew >= 180:
            MinutosNew -= 180
            HoraNew += 1
            break
        break
    break


print(f'{HoraNew}: {MinutosNew}')