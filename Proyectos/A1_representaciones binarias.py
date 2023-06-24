#b.	Leer  un entero  y  generar  un  string con su representación en binario

salida=0
while salida==0:
    numero=int(input('digite un numero: '))
    rta=1
    print('vamos a encontrar ese numero en representacion binaria')
    while rta!=0:
        rta=numero//2
        res=numero%2
        numero=rta
        print(res, end=' ')
    salida=int(input('\npara salir digite un numero diferente de cero: '))
print('fin')