'''Contador de letras: Programa que cuenta
la cantidad de cada una de las letras que
aparecen en una frase,incluso las que
no aparecen'''
import string
frase='Hoy ah salido el sol y hace mucho calor'
abecedario = string.ascii_lowercase
conteo=dict.fromkeys(abecedario,0)

for letra in frase.lower():#q la aumente
    if letra in conteo:
        conteo[letra]+=1

for le, nu in conteo.items():#que las cuente
    print('{}: {}'.format(le,nu))
