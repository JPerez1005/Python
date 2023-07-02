import string

alfabeto = string.ascii_uppercase#Letras mayusculas del abecedario
mensaje = 'ESTE MENSAJE ES SECRETO'#mensaje Predefinido
clave = 7#cantidad de movimientos que hace

cifrado = ''#cifrado como vacio

for letra in mensaje.upper():#para cada elemento en el mensaje
  if letra in alfabeto:#Para cada elemento en el alfabeto
    indice = alfabeto.find(letra)#en el alfabeto encontramos la posicion de las letras
    indice_cifrado = (indice + clave) % 26#el limite del abecedario es 27
    cifrado += alfabeto[indice_cifrado]#la nueva posicion
  else:
    cifrado += letra

print(cifrado)