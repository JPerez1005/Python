'''Pasar una lista bidimensional a dos listas
unidimensionales, y viceversa: dos listas unidimensionales
a una bidimensional'''

grupos=[[1,'A'],[2,'B'],[3,'C'],[4,'D'],[5,'E'],
        [6,'F'],[7,'G'],[8,'H'],[9,'I'],[0,'J']]

##numeros = [1,2,3,4,5,6,7,8,9,0]
##letras = ["A","B","C","D","E","F","G","H","I","J"]
#Tengo que pasar uns bidimensional a dos unidimensionales
numeros=[]
letras=[]
# for numero in grupos:
#     numeros.append(numero[0])
# for letra in grupos:
#     letras.append(letra[1])
for lista in grupos:
    numeros.append(lista[0])
    letras.append(lista[1])
print(numeros)
print(letras)

grupos2=[]

for i in range(len(numeros)):
    grupos2.append([numeros[i],letras[i]])
    #repaso de posiciones

print(grupos2)