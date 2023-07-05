miLista=[]#lista vacia
miLista=list()
print(miLista, len(miLista))
miLista.append('Julian')
print(miLista, len(miLista))
print(miLista[0:1])
miLista.extend(['Alejandro','Alejandro','Edwar'])#extiende la lista en la lista
miLista.append(['Alejandro','Alejandro','Edwar'])#agrega una lista dentro de la lista
print(miLista, len(miLista))
miLista.pop()#si no le indico la posicion borra el ultimo elemento,(borra posiciones)
miLista.insert(2, 'Lilian')#agrega el string en la posicion 2
miLista.remove('Lilian')
print(miLista,len(miLista))

print('------------------------------------------------------------------------')
'''Dos formas de recorrer la lista'''
#RECORRIDO POR INDICE
for elem in range(len(miLista)):
    print(elem)#elem devuelve las posiciones
    print(miLista[elem])#miLista[elem] devuelve el valor de esa posicion

print('------------------------------------------------------------------------')
#RECORRIDO POR ELEMENTO
for elem in miLista:
    print(elem)#a diferencia de indice no depende de la posicion, 
    #los imprime uno por uno el valor

print('------------------------------------------------------------------------')
#BUSCAR UN ELEMENTO SI ESTA DEVUELVE LA POSICION Y SINO (-1)
def BuscarElem(lst, elem):
    for i in range(len(lst)):
        if lst[i]==elem:
            return i#si lo encuentra devuelve el elemento
    return -1#Si no encuentra el elemento devuelve un menos 1
pos=BuscarElem(miLista, ' Julian')
print(pos)

print('------------------------------------------------------------------------')
#BUSCAR UN ELEMENTO EN LA LISTA. SI ESTÁ, DEVUELVE TRUE, SI NO FALSE
def encontrarElem(lst, elem):
    for e in lst:
        if e==elem:
            return e#si lo encuentra devuelve el elemento
    return False#Si no encuentra el elemento devuelve un false
esta=encontrarElem(miLista,'Alejandro')
print(esta)

#PARTA LIMPIAR TODA LA LISTA
miLista=miLista.index('Julian')#la forma mas rapida de buscar