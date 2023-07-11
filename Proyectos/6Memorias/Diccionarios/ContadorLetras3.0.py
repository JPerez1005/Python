'''Contador de letras: Programa que cuenta
la cantidad de cada una de las letras que
aparecen en una frase'''

frase='Hoy ah salido el sol y hace mucho calor'
frase=frase.lower()
letras=dict.fromkeys(frase,0)

for letra in frase:
    if letra in letras:
        letras[letra] += 1

print(letras)