'''Escribir una función que dada una cadena de
caracteres, devuelva:

1.) La primera letra de cada palabra.
Por ejemplo, si recibe Universal Serial Bus
debe devolver USB.

2.) Dicha cadena con la primera letra de cada
palabra en mayúsculas. Por ejemplo, si recibe
república argentina debe devolver República Argentina.

3.) Las palabras que comiencen con la letra A.
Por ejemplo, si recibe Antes de ayer debe devolver
Antes ayer.'''

def Siglas():
    mensaje9 = input('Digite una cadena de caracteres: ')
    mensaje9 = mensaje9.split()

    for elemento in mensaje9:
        mensaje9a = elemento[0]  # Acceder al primer carácter del elemento actual
        print(mensaje9a)

def Titulos():
    cadena=input('Digite una frase: ')
    print(cadena.title())
    if cadena.istitle()==True:
        print('Frase cambiada')
    else:
        print('No se pudo cambiar la frase')

def LetrasIniciales():
    mensaje9 = input('Digite una cadena de caracteres: ')
    mensaje9 = mensaje9.split()

    for palabra in mensaje9:
        if palabra.istitle() and palabra.startswith('A'):
            print(palabra[0:])
