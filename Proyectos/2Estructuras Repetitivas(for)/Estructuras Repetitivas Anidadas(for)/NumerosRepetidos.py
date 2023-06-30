'''Encontrar numeros repetidos de una lista'''

Numeros= [2,3,5,1,4,3,6,7,9,5,8]

Repetidos=[]

for i in range(len(Numeros)):
    for j in range(len(Numeros)):
        if i!=j:
            if Numeros[i]==Numeros[j] and Numeros[i] not in Repetidos:
                Repetidos.append(Numeros[i])

print(Repetidos)