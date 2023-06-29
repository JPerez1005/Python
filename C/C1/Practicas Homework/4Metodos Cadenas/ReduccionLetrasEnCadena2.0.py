"""Dada una cadena de caracteres en minúsculas que contiene
letras del rango ascii[‘a’..’z’], debes reducir la cadena
realizando una serie de operaciones.

En cada operación, selecciona un par de letras adyacentes
que sean iguales y elimínalas. Elimina tantos caracteres
como sea posible utilizando este método y devuelve la
cadena resultante. Si la cadena final está vacía,
devuelve "Empty String"."""

letter1 = ""
letter2 = ""
round = 1
verification = 1
print("\n\tReduccion de caracteres")

while True:
    word = input("Ingrese una serie de caracteres: ")
    if word.strip().isalpha():
        break
    else:
        print("Ingrese solo letras")
new_word = word

while True:
    for i in new_word.lower():
        if round % 2 != 0:
            letter1 = i
        if round % 2 == 0:
            letter2 = i
        round += 1
        if letter1 == letter2:
            new_word = new_word.replace(i,"",2)
            letter1 = ""
            letter2 = ""
    round = 1
    if new_word == "":
        new_word = "Cadena Vacia"
        break
    if len(new_word) == verification:
        break
    verification += 1

print(f"\nLa cadena resultante de la reduccion es: {new_word.strip()}\n")