"""Escribir un programa que pida al usuario una palabra 
y luego muestre por pantalla una a una las letras de 
la palabra introducida empezando por la última."""

palabras=input('Digite alguna palabra: ')

for letra in range(len(palabras)-1, -1, -1):
    print(palabras[letra])