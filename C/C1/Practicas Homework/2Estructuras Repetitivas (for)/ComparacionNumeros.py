"""Construya un programa que lea 10 números ingresados por el usuario y que al final, muestre el mayor
y el menor de todos estos números."""
NuevoNumMayor=float('-inf')#es la representacion del numero infinito negativo
NuevoNumMenor=float('inf')#es la representacion del infinito
for i in range(1,11):
    if i==1:
        Num=int(input(f'{i}.) Digite un Numero: '))
    elif i>1:
        Num=int(input(f'{i}.) Digite otro Numero: '))
    if Num>NuevoNumMayor:
        NuevoNumMayor=Num

    if Num<NuevoNumMenor:
        NuevoNumMenor=Num

print('-'*20, 'Resultado','-'*20,'\n')
print(f'El numero mayor es: {NuevoNumMayor}')
print(f'El numero menor es: {NuevoNumMenor}')
print('\n\n','-'*20, 'Fin','-'*20,'\n')