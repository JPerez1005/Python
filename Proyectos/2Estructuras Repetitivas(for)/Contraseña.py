"""Escribir un programa que almacene 
la cadena de caracteres contraseña 
en una variable, pregunte al usuario 
por la contraseña hasta que introduzca 
la contraseña correcta.
"""

Contra=input('Digite una contraseña: ')

for i in range(1,4):
    if Contra=='Julian' and i==3:
        print('Bienvenido Julian :)')
    elif Contra!='Julian':
        Contra=input('Digite una contraseña: ')
    elif i==3:
        print('El numero de intentos acabó, yo sé q a la proxima si lo logras')