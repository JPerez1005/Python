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
bandera = False
inicio = time()

for a in abc or abc2 or numeros:
    if bandera:#si bandera es falsa no entra en la condicion
        break
    for b in abc or abc2 or numeros:
        if bandera:#si bandera es falsa no entra en la condicion
            break
        for c in abc or abc2 or numeros:
            if bandera:#si bandera es falsa no entra en la condicion
                break
            for d in abc or abc2 or numeros:
                if bandera:#si bandera es falsa no entra en la condicion
                    break
                for e in abc or abc2 or numeros:
                    if bandera:#si bandera es falsa no entra en la condicion
                        break
                    if a == clave or a+b == clave or\
                    a+b+c == clave or a+b+c+d == clave\
                    or a+b+c+d+e == clave:
                        print("Clave encontrada:", clave)
                        bandera = True

final = time()
res = final-inicio

print(f"La clave tardó: {round(res,5)} segundos en encontrarse")