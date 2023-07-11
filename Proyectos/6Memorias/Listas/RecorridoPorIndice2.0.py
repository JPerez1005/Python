'''Recorrer una lista anidada y mostrar todos sus elementos,
pero no haciendo referencia a sus listas y a los elementos
de las listas, sino a los índices que ocupan sus elementos.

Una vez hecho esto, mostrar sólo las listas que contienen
letras de una lista anidada que contiene listas con números
y letras.'''

datos = [[1,2,3,4],
               ["a","b","c","d"],
               [5,6,7,8],
               ["e","f","g","h"],
               [9,10,11,12], 
               ["i","J","k","l"], 
               [13,14,15,16],
               ["m","n","ñ","o"]]

for fila in datos:
    for elemento in fila:
        print(elemento , end='')
    print()
