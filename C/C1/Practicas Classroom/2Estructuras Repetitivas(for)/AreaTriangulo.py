"""Algoritmo que nos calcule el área de un triángulo conociendo sus lados. La estructura selectiva
se utiliza para el control de la entrada de datos en el programa. Para calcular el área, usar la
siguiente fórmula:"""

l=0
a=0
b=0
c=0

for i in range(1,4):
    l=int(input(f'Digite el lado {i}: '))
    if i==1:
        a=l
    elif i==2:
        b=l
    elif i==3:
        c=l

p=(a+b+c)/2

area=(p*(p-a)*(p-b)*(p-c))**0.5

print('-'*5,'Resultado','-'*5,'\n')

print('El area del triangulo es: ',area)

if p>a and p>b and p>c:
    print('Cumple con las condiciones para ser un triangulo')
print('-'*5,'Fin','-'*5,'\n')