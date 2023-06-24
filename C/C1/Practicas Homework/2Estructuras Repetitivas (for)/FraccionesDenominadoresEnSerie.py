"""Construya un programa tal que lea un número entero N, muestre la cantidad de términos y el resultado
de la siguiente serie:"""

N=int(input('Digite un numero: '))
op1=0
op2=0
for i in range(1,N+1):
    if i%2==0:
        op2=(op2)-(1/i)
        print(f'-1/{i}')
    else:
        op1=(op1)+(1/i)
        print(f'+1/{i}')

opTotal=(op1+op2)

print('-'*20, 'Resultado','-'*20,'\n')
print('El resultado de la operacion de denominadores secuenciales es: \n{:.2f}'.format(opTotal))
print('\n\n','-'*20, 'Fin','-'*20,'\n')
