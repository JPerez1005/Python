'''Diseñar un algoritmo que calcule el máximo
común divisor de dos números mediante el
algoritmo de Euclides.
Sean los dos números A y B. El método para hallar
el máximo común divisor (mcd) de dos números A
y B por el método de Euclides es:

I. Dividir el número mayor (A) por el menor (B).
Si el resto de la división es cero, el número B
es el máximo común divisor.
II. Si la división no es exacta, se divide el
número menor (B) por el resto de la división
anterior.
III. Se siguen los pasos anteriores hasta obtener
un resto cero. El último divisor es el mcd
buscado.'''

def MCD():
    num1=int(input('digite un numero: '))
    num2=int(input('digite otro numero: '))

    if num2>num1 :
        reserva=num2
        num2=num1
        num1=reserva
    res=1
    while res!=0:
        cociente=num1//num2
        res=num1%num2
        num1=num2
        num2=res
    
    print('el maximo comun divisor es: ',num1)

    print('fin')

MCD()