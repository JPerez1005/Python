'''Juego que pregunta un numero del 1 al 5 y luego
una vocal. Tienes 100 puntos, si aciertas uno de ellos
te quita 2 puntos, si no aciertas ninguno, te quita
5 puntos.
El programa no se acaba hasta que aciertas los dos
.Cuando se acaba, el programa te dice los puntos
que te quedan'''

numero='3'
vocal='a'
puntos=100
jugando=True

while jugando:
    intento_n=input('Dime un numero del 1 al 5: ')
    intento_v=input('Dime una letra vocal: ')
    if intento_n!=numero and intento_v!=vocal:
        puntos-=5
        print('No has acertado ninguno. Te quedan ',
              puntos,' puntos')
    elif intento_n!=numero or intento_v!=vocal:
        puntos-=2
        print('No has acertado uno. Te quedan '
              ,puntos,' puntos')
    else:
        print('Has acertado. Tus puntos restantes son: '
              ,puntos)
        jugando=False

print('Fin del juego...')