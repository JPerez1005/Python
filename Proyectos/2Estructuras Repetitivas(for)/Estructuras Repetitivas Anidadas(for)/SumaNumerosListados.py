'''Comprobar si la suma  de dos numeros
de una lista dan como resultado 10, y
mostrar todas las soluciones. 
(No cuenta la suma de un numero consigo
mismo)'''

numeros=[2, 3, 5, 8, 4, 7, 6, 1]

for x in range(len(numeros)):#lee la posicion de cada numero
    for y in range(len(numeros)):#lee la posicion de cada numero
        if x!=y:#si las posiciones son diferentes entonces...
            suma=0
            suma=numeros[x]+numeros[y]#sumamos los valores de los numeros no las posiciones
            if suma==10:
                print(f'la suma entre {numeros[x]} y {numeros[y]} es: {suma}')
