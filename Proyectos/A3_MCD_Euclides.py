#hallar el maximo comun divisor de dos numeros con el metodo de euclides

salida=0

while salida==0:
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

    salida=int(input('si quiere seguir digite el numero cero(0): '))

print('fin')