lista=[]
numeros=0
def menu():
    print('Menu\n')
    print('1.) Crear lista')
    print('2.) colocar numeros')
    opcion=int(input('Digite una opcion: '))
    if opcion==1:
        while True:
            car=input('Digite un caracter: ')
            lista.extend(car)
            des=input('Quiere seguir digitando caracteres?(s/n): ').lower()
            if des=='n':
                break
        
        print(lista)
        if lista.isinstance(lista,list)==True:
            print('Es una lista')
    elif opcion==2:
        while True:
            numeros=int('Digite un numero')
            des=input('Quiere seguir digitando caracteres?(s/n): ').lower()
            if des=='s':
                break
        print(numeros)
        if numeros.isinstance(numeros,int)==True:
            print('Es un numero')


menu()
        