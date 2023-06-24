"""Mostrar en pantalla si dos números enteros positivos n1 y n2 son amigos. Los números amigos son pares
de números enteros positivos en los cuales la suma de los divisores propios de cada número es igual al
otro número. En otras palabras, dos números amigos cumplen la condición de que la suma de los
divisores propios de uno de ellos es igual al otro número, y viceversa. Por ejemplo, el par de números
(220, 284) es un par de números amigos. Los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44,
55 y 110. Si sumamos estos números, obtenemos 284, que es el segundo número del par. Por otro lado,
los divisores propios de 284 son 1, 2, 4, 71 y 142, y si los sumamos, obtenemos 220, que es el primer
número del par."""

num=int(input('Digite un numero: '))
num2=int(input('Digite otro numero: '))
SFriend=0
SFriend2=0

print('-'*5,'Resultado','-'*5,'\n')
for i in range(1,num):
    if num%i==0:
        SFriend=SFriend+i#se suman los numeros que se van guardando
        print(SFriend, end=', ')
print('\n')
for i in range(1,num2):
    if num2%i==0:
        SFriend2=SFriend2+i#se suman los numeros que se van guardando
        print(SFriend2, end=', ')

print('')

if SFriend==num2 and SFriend2==num:
    print('\nEsos dos numeros son muy buenos amigos')
else:
    print('\nlos numeros son liebres')
print('-'*5,'Fin','-'*5,'\n')