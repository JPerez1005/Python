"""Contador de vocales: Crea un programa que solicite al usuario ingresar una frase y cuente la cantidad
total de vocales en ella. Utiliza un ciclo "while" para recorrer cada letra de la frase. Si una vocal es
encontrada, incrementa el contador de vocales. Sin embargo, si el usuario ingresa la letra 'q', el programa
debe terminar y mostrar la cantidad total de vocales encontradas hasta ese momento."""

frase=''
cont=0
while frase!='q':
    frase=input('Ingrese una frase(ingrese q para salir): ')
    if frase.isalpha():
        for x in 'aeiou':
            if x in frase:
                cont=cont+1
        print(f'\nHay un total de {cont} vocales en esa frase')
    else:
        print('No ingrese numeros en el programa')
