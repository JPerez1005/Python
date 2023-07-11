'''Aplanar una lista anidada que contiene
tanto listas como numeros enteros'''

datos=[[1,2,3],4,5,[6,7],8,9]

plana=[]

for dato in datos:
    if isinstance(dato,int):
        plana.append(dato)
    elif isinstance(dato,list):
        for elemento in dato:
            plana.append(elemento)

print(plana)