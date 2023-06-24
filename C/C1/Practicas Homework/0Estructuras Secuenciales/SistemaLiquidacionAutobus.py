"""Se desea liquidar el valor a pagar a un conductor de una buseta de transporte intermunicipal. Se
conoce el nombre, placa del vehículo, valor total por concepto de pasajes y el valor total por concepto
de encomiendas. Si por el valor de los pasajes se le liquida el 25% y por el valor de encomiendas se le
liquida el 15%, se pide calcular el valor total a pagar al conductor. Se debe visualizar, el nombre, placa
del vehículo, valor total pasajes, valor a pagar por concepto de pasaje, valor total encomiendas, valor a
pagar por concepto de encomiendas y el valor total a pagar al conductor.
"""

print('----SISTEMA DE LIQUIDACIÓN DE CONDUCTORES DE AUTOBUS----')

Nombre = ''
Placa = ''

while Nombre == '' or not Nombre.replace(' ', '').isalpha() or len(Nombre)<=2:
    Nombre = input('Ingrese el nombre del conductor: ')

while Placa == '' or not Placa.replace(' ', '') or len(Placa)<=6:
    Placa = input('Ingrese la placa del vehículo: ')

Dinero = float(input('Ingrese el valor de los pasajes: '))
Dinero2 = float(input('Ingrese el valor de las encomiendas: '))

NumPasajeros = int(input('Ingrese el numero de pasajeros: '))
NumEncomiendas = int(input('Ingrese el numero de encomiendas que hizo el conductor: '))

ValorTotalPasajes = round(float(Dinero*NumPasajeros),2)
ValorTotalEncomiendas = round(float(Dinero2*NumEncomiendas),2)

ValorPagoPasajes =round( float(ValorTotalPasajes*0.25),2)
ValorPagoEncomiendas = round(float(ValorTotalEncomiendas*0.15),2)
ValorTotal=ValorPagoPasajes+ValorPagoEncomiendas



print('-----------RESULTADO------------')

print(f'Nombre :{Nombre}\nPlaca :{Placa}\nValor total de los pasajes: {ValorTotalPasajes}\nValor por concepto de pasajeros: {ValorPagoPasajes}\nValor total de las encomiendas: {ValorTotalEncomiendas}\nValor por concepto de encomiendas: {ValorPagoEncomiendas}\nEl pago total del conductor es: {ValorTotal}')

print('-----------------Fin------------------')