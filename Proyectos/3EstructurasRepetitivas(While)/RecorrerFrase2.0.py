'''Solicitar al usuario el ingreso de una frase
y de una letra (que puede o no estar en la frase).
Recorrer la frase, carácter a carácter,
comparando con la letra buscada. Si el carácter
no coincide, indicar que no hay coincidencia en
esa posición (imprimiendo la posición) y
continuar. Si se encuentra una coincidencia,
indicar en qué posición se encontró y finalizar
la ejecución.'''

frase=input("Frase: ")
l=input("Letra para buscar su posición: ")
i=0
while i!=len(frase):#con len podemos recorrer las
    #posiciones de las frases
    if l!=frase[i]:
        print("No se encontró en la posición", i)
        i+=1#tambien podemos sumar las veces
        #que se repite
        continue
    print("Se encontró en la posición", i)
    break