'''Comprobar si la suma  de dos numeros
de una lista dan como resultado 10, y
mostrar todas las soluciones. 
(No cuenta la suma de un numero consigo
mismo)'''

numeros=[2, 3, 5, 8, 4, 7, 6, 1]

Parejas=[]

for x in range(len(numeros)):
    sumando=10-numeros[x]
    if sumando in numeros and numeros.index(sumando)!=x:#si el numero esta repetido no entra
        pareja=sorted([numeros[x], sumando])
        if pareja not in Parejas:
            Parejas.append(pareja)

print(Parejas)
