"""Escribir un programa que muestre el eco de todo lo
 que el usuario introduzca hasta que el usuario escriba 
 “salir” que terminará."""

for i in range(0,100):
    frase= input('Digite cualquier palabra o frase: ')
    if frase=='salir':
        print('Saliendo...')
        break
    print(frase)
