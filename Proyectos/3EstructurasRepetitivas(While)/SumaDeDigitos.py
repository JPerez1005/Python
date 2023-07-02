'''Leer un número entero positivo desde teclado
e imprimir la suma de los dígitos que lo componen.'''


suma=0#La suma inicia en cero
n=int(input("Número positivo: "))#se ingresa un numero
while n!=0:#mientras el numero no sea 0, pues entre
    digito=n%10#el residuo de aquel numero se guarda
    suma+=digito
    n=n//10
print("Suma de los dígitos:", suma)