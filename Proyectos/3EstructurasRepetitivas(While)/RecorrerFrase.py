'''Solicitar al usuario el ingreso de una frase
y de una letra (que puede o no estar en la frase).
Recorrer la frase, carácter a carácter, comparando
con la letra buscada. Si el carácter no coincide,
indicar que no hay coincidencia en esa posición
(imprimiendo la posición) y continuar. Si se
encuentra una coincidencia, indicar en qué
posición se encontró y finalizar la ejecución.'''

Frase=input('Digite una frase: ')
Letra=input('Digite una letra: ')
if Letra in Frase:
    print('La letra está en la frase...')
    indice = Frase.find(Letra)
    print(f'La letra está en la posicion: {indice+1}')
else:
    print('La letra no está en la frase...')