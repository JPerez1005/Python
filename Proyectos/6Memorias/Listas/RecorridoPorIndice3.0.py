'''Una vez hecho esto, mostrar sólo las listas que contienen
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

for i in range(len(datos)):#con i recorro numeros
    #de filas
    if i%2!=0:#si i es diferente a par
        for j in range(len(datos[i])):
            #j recorre los datos impares
            print(datos[i][j], end='')
        print()
