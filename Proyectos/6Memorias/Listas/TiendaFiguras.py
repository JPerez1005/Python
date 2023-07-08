'''En una tienda quieren hacer un inventario de las
figuras que tienen y el numero de unidades de cada
una. crea una lista que contenga los datos del invent
ario: 6 cuadrados, 5 circulos, 4 triangulos y 3
rectangulos'''

figuras=[['Cuadrados',6,[3,1]],
         ['Círculos',5,[1,2]],
         ['Triangulos',4,[2,2]],
         ['Rectangulos',3,[4,3]]]

figuras[0][1]=5#apartir del index cambiamos la cantidad
figuras[0][2]=[1,3]
#se hizo cambio de la lista en la posicion 2
figuras[3][2][0]=2
#se hizo el cambio en la tercera lista anidada solo un
#dato
for f in figuras:
    print('{:12}: {:2}. Columna: {}. Fila {}'
          .format(f[0],f[1],f[2][0],f[2][1]))