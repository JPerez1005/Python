"""  """
nombre=input('Digite su nombre: ')
c=int(input('Digite su calificacion: '))

if c<0:
    print('Has digitado un valor no valido\n')
elif c<60:
    cual='D'
    print(f'{nombre} su calificacion cuantitativa es: {c}')
    print(f'y su calificacion cualitativa es: {cual}\n')
elif c<80:
    cual='C'
    print(f'{nombre} su calificacion cuantitativa es: {c}')
    print(f'y su calificacion cualitativa es: {cual}\n')
elif c<90:
    cual='B'
    print(f'{nombre} su calificacion cuantitativa es: {c}')
    print(f'y su calificacion cualitativa es: {cual}\n')
elif c<=100:
    cual='A'
    print(f'{nombre} su calificacion cuantitativa es: {c}')
    print(f'y su calificacion cualitativa es: {cual}\n')
else:
    print('has digitado un valor no valido\n')
    
print('-'*5,'Fin',5*'-')
