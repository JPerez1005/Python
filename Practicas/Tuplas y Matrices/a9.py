#el uso de las tuplas

tp1=tuple()#es una tupla
print(type(tp1))

tp2=("hola",)#es otro metodo de tupla
print(type(tp2))

tp3=("hola")
print(type(tp3))#me muestra el tipo de parametro

lista=list("hola")#convierte las palabras en lista como el for in
print(lista)

tp3=tuple(lista)#convierte la lista en tupla
print(tp3)