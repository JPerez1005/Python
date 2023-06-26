"""Realizar un programa que lea los lados de n triángulos.
 Informar después de cada triángulo si es equilátero 
 (tres lados iguales), isósceles (dos lados iguales) 
 o escaleno (ningún lado igual). Informar después del 
 total de triángulos de cada tipo."""

CantTriangulos=int(input('Digite la cantidad de triangulos: '))
a=0
b=0
c=0
for t in range(1,CantTriangulos+1):
    for l in range(1,4):
        lado=float(input(f'Digite un lado del triangulo {t}: '))
        if l==1:
            a=lado
        elif l==2:
            b=lado
        else:
            c=lado
    if a==b==c:
        print(f'El triangulo es equilatero')
    elif a==b!=c or a!=b==c:
        print(f'El triangulo es isósceles')
    else:
        print(f'El triangulo es escaleno')