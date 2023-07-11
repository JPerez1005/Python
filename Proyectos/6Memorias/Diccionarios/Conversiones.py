'''Convertir un diccionario en dos listas: 
pares = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}

Convertir dos listas en un diccionario:
letras = ["A", "B", "C", "D", "E"]
numeros = [1,2,3,4,5]'''

numeros=[]
letras=[]
pares={"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}

numeros=list(pares.values())
letras=list(pares.keys())
print(numeros)
print(letras)
pares={}
pares=dict(zip(letras,numeros))
print(pares)