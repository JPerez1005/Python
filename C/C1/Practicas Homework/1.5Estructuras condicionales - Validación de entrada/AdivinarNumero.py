"""Adivina el número: Crea un programa en el que la computadora "piense" un número secreto entre 1 y
100, y el usuario tenga que adivinarlo. El programa debe proporcionar pistas como "Demasiado bajo"
o "Demasiado alto" hasta que el usuario adivine correctamente.
El usuario que gana es el que adivine en el menor número de intentos.
Este programa se hizo en clase. Para el software review modifícalo para que el usuario tenga un limite
de 3 a 5 intentos (escoja un número al azar entre [3, 5]. Cada usuario puede tener un número de intentos
distinto) para adivinar el número."""
import random#es necesario para colocar numeros random
numero=random.randint(1,11)#del 1 al 100
NumeroIntentos=random.randint(3,6)#del 3 al 5
jugando=True#no es necesario, lo tengo ahi como por que sí
Usuarios=int(input('Cuantos usuarios jugarán?: '))#los usuarios que van a jugar
Cont=0
NombreMenor=''#el nombre con menos intentos es el que se mostrará
IMenor=float('inf')

for x in range(1,Usuarios+1):#está conectada con la variable usuario, de cuantos juegan
    nombre=input('Digite su nombre: ')#se guarda el nombre en la variable nombre
    try:
        while Cont<NumeroIntentos:
            Num=int(input('ingrese un numero: '))
            if Num==numero:
                print('Felicidades has ganado!!')
                print('El numero era: ',numero)
                print(f'Lo adivinaste en: {Cont} veces.')
                if Cont<IMenor:
                    IMenor=Cont
                    NombreMenor=nombre
                break
            elif Num<numero:
                print('Demasiado bajo...')
                print('sigue intentando')
            elif Num>numero:
                print('Demasiado alto...')
                print('sigue intentando')
            Cont=Cont+1
    except ValueError:
        print("!Error!. Debes ingresar un numero válido...")

print('\n','-'*10,'Resultado del Ganador {}'.format(NombreMenor),'-'*10)
print(f'El usuario con menos intentos fue {NombreMenor} con {IMenor}')
print('\n','-'*10,'Fin','-'*10)