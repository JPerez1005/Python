#IMPRESION DE NUMEROS PARES

#hacemos uso de omitir iteraciones en los ciclos

cont=0

while cont<10:
    if(cont%2)==1: #miramos que numeros son impares
        cont=cont+1
        continue #ignoramos los impares
    else:
        print('contador = ',cont)
        cont=cont+1

print('/nFin del programa')
