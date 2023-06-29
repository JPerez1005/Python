"""Dada una cadena de caracteres en minúsculas que contiene
letras del rango ascii[‘a’..’z’], debes reducir la cadena
realizando una serie de operaciones.

En cada operación, selecciona un par de letras adyacentes
que sean iguales y elimínalas. Elimina tantos caracteres
como sea posible utilizando este método y devuelve la
cadena resultante. Si la cadena final está vacía,
devuelve "Empty String"."""

vacia=True
while True:
    Cadena = input("Ingrese cadena de caracteres: ")
    if Cadena.strip() == "":#despues de eliminar cualquier espacio se verifica si la cadena está vacia
        print("Error. Cadena vacia.")
        continue
    break

Min=False
for c in Cadena:
    ascii = ord(c)
    # validar si hay Minuscula
    if ascii >= 97 and ascii <= 122 or ascii == 164:
        Min = True
        repetida = False
        for a in Cadena:
            if a==c:
                print(c)
    else:
        print('los caracteres no estan en minuscula')
