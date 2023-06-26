"""Programa que pide que adivines un numero del
1 al 10, cuando lo adivinas se para."""
import random
numero=random.randint(1,11)
jugando=True

for i in range(1,100):
    Num=int(input('ingrese un numero o cero(0) para salir: '))
    if Num==numero:
        print('Felicidades has ganado!!')
        print('El numero era: ',numero)
        print(f'Lo adivinaste en: {i} veces.')
        break
    elif Num==0:
        print('Elegiste salir, el numero era: ',numero)
        print('Saliendo...')
        break
    elif Num<0 or Num>10:
        print('El numero ingresado no es valido!!')
        print('Intenta colocar numeros mayores a cero')
        print('y numeros menores a diez')
    elif Num!=numero:
        print('sigue intentando')

print('\n','-'*10,'Fin','-'*10)
