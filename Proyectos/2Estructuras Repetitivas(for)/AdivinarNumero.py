"""Programa que pide que adivines un numero del
1 al 10, cuando lo adivinas se para.(vale)"""
import random#es necesario para colocar numeros random
numero=random.randint(1,101)#del 1 al 100
jugando=True#no es necesario, lo tengo ahi como por que sí
Usuarios=int(input('Cuantos usuarios jugarán?: '))#los usuarios que van a jugar
intentos=float('inf')#el numero de intentos es infinito, no se si está claro
NombreMayor=''#el nombre con menos intentos es el que se mostrará


for x in range(1,Usuarios+1):#está conectada con la variable usuario, de cuantos juegan
    nombre=input('Digite su nombre: ')#se guarda el nombre en la variable nombre
    for i in range(1,100):#el numero de intentos es 100 en este caso
        Num=int(input('ingrese un numero o cero(0) para salir: '))#el numero que ingresara el
        #usuario,
        if Num==numero:
            print('Felicidades has ganado!!')
            print('El numero era: ',numero)
            print(f'Lo adivinaste en: {i} veces.')
            if intentos>i:
                intentos=i
                NombreMayor=nombre#es verda
            break
        elif Num<numero:
            print('Demasiado bajo')
            print('sigue intentando')
        elif Num>numero:
            print('Demasiado alto')
            print('sigue intentando')
        elif Num==0:
            print('Elegiste salir, el numero era: ',numero)
            print('Saliendo...')#
            break
        elif Num<0 or Num>100:#try si señor
            print('El numero ingresado no es valido!!')
            print('Intenta colocar numeros mayores a cero')
            print('y numeros menores a diez')

print(f'El usuario con menos intentos fue {NombreMayor} con {intentos}')
print('\n','-'*10,'Fin','-'*10)
