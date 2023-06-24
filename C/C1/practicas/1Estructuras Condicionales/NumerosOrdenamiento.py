"""Diseñe y escriba un programa que solicite tres 
números enteros (pueden ser positivos o negativos) y
como salida los muestre en orden de mayor a menor."""

mayor = 0
mediano = 0
menor = 0


n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

print('-'*10, 'Resultado','-'*10,'\n')


if n1 > n2 and n1 > n3:
    mayor=n1
    if n2>n3:
        mediano=n2
        menor=n3
    else:
        mediano=n3
        menor=n2
elif n2 > n1 and n2 > n3:
    mayor=n2
    if n1>n3:
        mediano=n1
        menor=n3
    else:
        mediano=n3
        menor=n1
else:
    mayor=n3
    if n1>n2:
        mediano=n1
        menor=n2
    else:
        mediano=n2
        menor=n1

print("El número mayor es: ", mayor)
print("El número mediano es: ", mediano)
print("El número menor es: ", menor)

print('\n','-'*10,'Fin' ,'-'*10)