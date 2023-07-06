'''Se desea realizar un programa en el cual se ingrese
N letras del abecedario, las cuales se deben almacenar
en una lista. Una vez creada la lista, se desea conocer
e imprimir la cantidad de 'a', la cantidad de 'e', la
cantidad de 'i', la cantidad de 'o', la cantidad de 'u'. 
que se encuentran en la lista
'''
while True:
    frase=input('Ingrese una frase: ')
    if frase.isdigit()==True:
        print('No digite numeros')
    else:
        break

contA=0
contE=0
contI=0
contO=0
contU=0
frase=list(frase)
for letra in frase:
    if letra=='a':
        contA+=1
    elif letra=='e':
        contE+=1
    elif letra=='i':
        contI+=1
    elif letra=='o':
        contO+=1
    elif letra=='u':
        contU+=1

print(f'La cantidad de a en esa frase es: {contA}')
print(f'La cantidad de e en esa frase es: {contE}')
print(f'La cantidad de i en esa frase es: {contI}')
print(f'La cantidad de o en esa frase es: {contO}')
print(f'La cantidad de u en esa frase es: {contU}')