'''Encontrar numeros repetidos de una lista'''

ListaNueva=[]

for i in range(1,11):
    Num=input('Digite algún numero: ')
    ListaNueva.append(Num)

Repetidos=[]

for i in range(len(ListaNueva)):
    for j in range(len(ListaNueva)):
        if i!=j:
            if ListaNueva[i]==ListaNueva[j] and ListaNueva[i] not in Repetidos:
                Repetidos.append(ListaNueva[i])

print(Repetidos)