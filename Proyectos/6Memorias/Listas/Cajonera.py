'''Inventario de las letras que se guardan
en una cajonera'''

cajonera=[
    [
        [['A',11],['B',12],['C',8],['D',6],['E',9]],
        [['F',15],['G',32],['H',16],['I',9],['J',4]],
        [['K',12],['L',21],['M',10],['N',7],['Ñ',12]],
    ],
    [
        [['O',8],['P',13],['Q',8],['R',16],['S',19]],
        [['T',31],['U',11],['V',23],['W',15],['X',3]],
        [['Y',14],['Z',23],[' ',0],[' ',0],[' ',0]],
    ]
]

print()
print('Cajonera'.center(50))
print()



while True:
    print()
    print('1.) Mostrar inventario')
    print('2.) Venta de letra')
    print('3.) Reposición de letra')
    print('4.) Salir...')

    opcion=input('-->: ')
    if opcion.isalpha()==True:
        print('No se admiten letras')
        continue#reinicia bucle
    if opcion=='1':
        for cajon in cajonera:#uso la sublista, hay dos
            for fila in cajon:#uso de las sublistas de las sublistas, hay tres
                for espacio in fila:#uso de las sublistas internas, hay 5
                    print('{:1}:{:2}    '.format(espacio[0], espacio[1]),end='')
                    #mostramos el indice de las sublistas internas
                print()
            print()
    elif opcion=='2':
        letra=input('Introduce la letra: ').upper()
        cantidad=int(input('Introduce cantidad: '))
        for cajon in cajonera:
            for fila in cajon:
                for espacio in fila:
                    if espacio[0]==letra:#si el espacio es igual a la letra
                        #que se quiere vender, entonces: 
                        espacio[1]-=cantidad
                        #a ese espacio le restamos la cantidad
                        if espacio[1]<0:
                            espacio[1]=0
                            print('Quedó vacía la lista')
    elif opcion=='3':
        letra=input('Dime la letra: ').upper()
        cantidad=int(input('Dime la cantidad: '))
        for cajon in cajonera:
            for fila in cajon:
                for espacio in fila:
                    if espacio[0]==letra:
                        espacio[1]+=cantidad
    elif opcion=='4':
        break
    else:
        print('Esa opción no existe...')