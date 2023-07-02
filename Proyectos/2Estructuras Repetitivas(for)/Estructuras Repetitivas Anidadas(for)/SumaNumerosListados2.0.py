'''Comprobar si la suma  de dos numeros
de una lista dan como resultado 10, y
mostrar todas las soluciones. 
(No cuenta la suma de un numero consigo
mismo)'''

numeros=[2, 3, 5, 8, 4, 7, 6, 1]

Parejas=[]

for x in numeros:
    if 10-x in numeros:#si 10-x está en numeros entonces...
        Pareja=sorted([x, 10-x])
        if Pareja not in Parejas:
            Parejas.append(Pareja)

print(Parejas)
