'''Cree una función que retorne el número de palabras
presentes en un String que le llega cómo parámetro.

(obs: considere que toda palabra válida está separada
por un espacio de la anterior)'''

def NumeroDePalabras():
    Oracion=input('Digite una oracion: ')

    if Oracion.isdigit():
        while True:
            print('No se admiten numeros...')
            Oracion=input('Digite una oracion: ')
            if not Oracion.isdigit():
                break

    espacios=Oracion.split(' ')
    print(len(espacios))


NumeroDePalabras()