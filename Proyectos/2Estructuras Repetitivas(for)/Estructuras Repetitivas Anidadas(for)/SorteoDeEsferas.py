"""En una loteria hay un bombo que tiene 10 esferas,
con los números de 1 al 10.
En un sorteo se sacan 5 esferas, 
sin que se introduzcan las esferas que se han sacado
previamente. Haz un programa que muestre todas las
apuestas posibles, es decir, todas las posibles 
combinaciones que se pueden dar en esa loteria.

Incluye un contador para comprobar el número de 
combinaciones que se dan.
"""
cont=0
Combinaciones=[]
for D in range(1,11):
    for A in range(1,11):
        for V in range(1,11):
            for I in range(1,11):
                for B in range(1,11):
                    if D!=A and D!=V and D!=I and D!=B and\
                       A!=V and A!=I and A!=B and\
                       V!=I and V!=B and I!=B:
                        comb=[D,A,V,I,B]
                        comb.sort()
                        if comb not in Combinaciones:
                            cont+=1
                            Combinaciones.append(comb)
                            print(comb)

print('Hubo un total de {}'.format(cont),' Resultados.')