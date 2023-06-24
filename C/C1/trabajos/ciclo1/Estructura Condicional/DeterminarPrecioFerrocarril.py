"""Determinar el precio de un billete de ida y vuelta en ferrocarril,
conociendo la distancia a recorrer y sabiendo que si el número de 
días de estancia es superior a siete y la distancia superior a 800
kilómetros el billete tiene una reducción del 30%. El precio por 
kilómetros es de 2500 pesos."""

PrecioKM=2500
Distancia=int(input("Ingrese la distancia a recorrer: "))
Dias=int(input("Ingrese el número de días de estancia: "))
Operacion=PrecioKM*Distancia
if Distancia>800 and Dias>7:
    Operacion=Operacion*0.3
    print('El pasajero tiene una reduccion del 30%\n')

print('-'*10, 'Resultado','-'*10,'\n')
print("El precio del billete es: ",Operacion,'\n')
print('-'*10, 'Fin','-'*10,'\n')
