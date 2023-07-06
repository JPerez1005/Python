'''Ejemplo1
Hacer un programa que ayude a un profe con las notas de estudiantes
El profesor ingresa la nota de los 10 estudiantes y el programa le muestra 
el promedio de las notas, la nota mayor, la nota menor y las tres primeras 
notas de mayor a menor
'''

def leerFloat(msg):
    while True:
        try:
            n=float(input(msg))
            if n<0 or n>5:
                print('Error!! Ingrese un codigo valido...')
                input('digite cualquier tecla para continuar....')
                continue#Para que vuelva y pregunte
            return n#Se sale de todo
        except ValueError:#Para solo numeros
            print('Error!. Ingrese un numero entero valido.')

notMen=-1
notMay=6
sumNotas=0
promNotas=0.0
listNotas=[]
for nest in range(1,11):
    nota=leerFloat(f'Ingrese nota estudiante #{nest}: ')
    listNotas.append(nota)
notMen=min(listNotas)#saca el menor de una lista
notMay=max(listNotas)#saca el mayor de una lista
promNotas=sum(listNotas)/len(listNotas)#Suma la lista y la divide por el numero de lista

print(f'La nota menor es {notMen}')
print(f'La nota mayor es {notMay}')
print(f'El promedio de las notas es: ',promNotas)
listNotas.sort(reverse=True)#primero ordenamos
tresNotas=listNotas[0:3]
strNotas=''
for nota in tresNotas:
    strNotas+=str(nota)+', '
    print('Las tres mejores notas son: ',strNotas)#join recibe la lista de las tres notas