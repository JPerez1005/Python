'''Diseñar una funcion que calcule la media de tres numeros
leidos del teclado y poner un ejemplo de su aplicacion'''
def LeerInt(msg):
    while True:
        try:
            n=int(input(msg))
            return n#Se sale de todo
        except ValueError:
            print('Error!. Ingrese un numero entero valido.')

def media(n1,n2,n3):
    m=(n1+n2+n3)/3
    return m

a=LeerInt('Ingrese el Primer numero: ')
b=LeerInt('Ingrese el Segundo numero: ')
c=LeerInt('Ingrese el Tercer numero: ')
prom=media(a,b,c)

print(f'La media de {a}, {b}, {c} es {prom:.3f}')#tres decimales