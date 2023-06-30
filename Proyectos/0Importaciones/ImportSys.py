import sys

Intervalo=range(1,10)
Lista=list(range(10))

BytesIntervalo=sys.getsizeof(Intervalo)
BytesLista=sys.getsizeof(Lista)

print(BytesIntervalo)
print(BytesLista)

'''Si nosotros ejecutamos esta programa nos mostrará
lo que pesa cada variable, en este caso pesa menos
el range, por lo cual es mejor usar range en el 
uso de secuencias de numeros, ya que pesa menos que
las listas'''