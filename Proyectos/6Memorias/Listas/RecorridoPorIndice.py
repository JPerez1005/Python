'''En este video resolvemos el reto de recorrer
una lista anidada a través de los índices de sus
listas y los elementos de estas listas.

A su vez llevamos a cabo la tarea de mostrar sólo
las listas de la lista anidada que contenían
letras, es decir, las que tienen índices impares:
'''

datos=[[1,2,3,4],
       ['a','b','c','d'],
       [5,6,7,8],
       ['e','f','g','h'],
       [9,10,11,12],
       ['i','j','k','l'],
       [13,14,15,16],
       ['m','n','ñ','o']]

for i in range(len(datos)):
    for j in range(len(datos[i])):
        print(datos[i][j], end=' ')
    print()