'''Programa que pide el usuario y la contraseña
Si no pones los dos correctamente te los vuelve
a pedir'''

usuario='Julian'
contrasena='Madre123'

print('BIENVENIDO AL SISTEMA')

entrando=True

while entrando:
    intento_u=input('Introduce el usuario: ')
    intento_c=input('Introduce la contraseña: ')
    if intento_u==usuario and intento_c==contrasena:
        print('Usuario y contraseña correctos!!')
        entrando=False
    else:
        print('Usuario y contraseña incorrectos')

print('Estamos en el sistema.')