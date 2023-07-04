cadena = "Hola mundo!"
tabla_de_sustitucion = str.maketrans("aeiou", "12345")
resultado = cadena.translate(tabla_de_sustitucion)
print(resultado)
