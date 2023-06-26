"""Solicitar al usuario que ingrese una frase 
y luego imprimir un listado de las vocales que 
aparecen en esa frase (sin repetirlas)."""

frase=input("Frase: ")
print("Vocales en la frase:")
for x in "aeiou":#la x recorre todas las vocales secuencialmente
  if x in frase:#si alguna de esas vocales está en la frase, se imprime
    print(x)