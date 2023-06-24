# Ejemplo de programa para leer una matriz por consola

print('Lectura de matriz A')
fa = int(input('Filas de A: '))#definimos el numero de filas
ca = int(input('Columnas de A: '))#definimos el numero de columnas

mata = []#creamos la lista principal
for i in range(fa):#recorremos desde i(0) hasta el numero de filas
    print('Lectura de la fila {}'.format(i))#las llaves y el formato de i se complementan
    #eso se hace para mostrar en que parte de la fila está
    fil = []#creamos la lista temporal
    for j in range(ca):#primero recorre todas las columnas de una fila y despues pasa a
        #recorrer todas las filas de la siguiente columna
        print(f'a({i},{j}) = ')
        num = int(input(': '))#el usuario digita el numero de esa casilla
        fil.append(num)

    mata.append(fil)

print(mata)
