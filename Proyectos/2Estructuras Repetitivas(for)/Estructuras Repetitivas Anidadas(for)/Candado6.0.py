"""Programa que adivina una clave, mediante fuerza bruta
El programa termina una vez encontrada la clave
La clave puede tener entre 1 y 5 caracteres"""
# !@#$%^&*()-_+=~`[]|:;"<>?,./

from time import time
import string
clave = input("Dime una clave con 5 minúsculas: ")
abc = string.ascii_lowercase 
abc2= string.ascii_uppercase
numeros = list(range(10))

inicio = time()

for c1 in abc or abc or numeros:
    if c1 

final = time()
res = final-inicio

print(f"La clave tardó: {round(res,5)} segundos en encontrarse")