"""Construya un programa que muestre los números divisibles de 3 y 7 entre 1 y 1000."""
num=3
num2=7

print('-'*20, 'Resultado','-'*20,'\n')
print('-'*10, 'Numeros Divisibles entre 3','-'*10,'\n')
for i in range(1,1000):
    if i%3==0:
        print(f'#{i}#', end=', ')

print('\n\n','-'*10, 'Numeros Divisibles entre 7','-'*10,'\n')
for i in range(1,1000):
    if i%7==0:
        print(f'#{i}#', end=', ')

print('\n\n','-'*20, 'Fin','-'*20,'\n')
