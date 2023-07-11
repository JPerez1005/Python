'''Contador de letras: Programa que cuenta
la cantidad de cada una de las letras que
aparecen en una frase'''

frase='Hoy ah salido el sol y hace mucho calor'

conteo={}

for letra in frase.lower():
    if letra not in conteo:
        conteo[letra]=1
    else:
        conteo[letra]+=1


ordenado={k:conteo[k] for k in sorted(conteo)}
print(ordenado)
