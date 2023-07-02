'''Programa que pide el usuario y la contraseña
Si no pones los dos correctamente te los vuelve
a pedir'''

usuario='Julian'
contrasena='Madre123'

print('BIENVENIDO AL SISTEMA')

intento_u=input('Introduce el usuario: ')
intento_c=input('Introduce la contraseña: ')

while intento_u!=usuario or intento_c!=contrasena:
    print('Usuario o contraseña incorrectos!!')
    intento_u=input('Introduce el usuario: ')
    intento_c=input('Introduce la contraseña: ')
else:
    print('Usuario y contraseña incorrectos')

print('Estamos en el sistema.')