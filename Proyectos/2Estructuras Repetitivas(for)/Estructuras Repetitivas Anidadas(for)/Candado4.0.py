"""Programa que adivina una clave, mediante fuerza bruta
El programa termina una vez encontrada la clave
La clave puede tener entre 1 y 5 caracteres"""
# !@#$%^&*()-_+=~`[]|:;"<>?,./
import time
import string

Clave=input('Dime una clave: ')
Alfabeto=string.ascii_lowercase
Intento=None

inicio=time.time()

for c1 in Alfabeto:
    if Intento!=Clave:#Si todavía no se encuentra la clave, sigue buscando...
        for c2 in Alfabeto:
            if Intento!=Clave:#Si todavía no se encuentra la clave, sigue buscando...
                for c3 in Alfabeto:
                    if Intento!=Clave:#Si todavía no se encuentra la clave, sigue buscando...
                        for c4 in Alfabeto:
                            if Intento!=Clave:#Si todavía no se encuentra la clave, sigue buscando...
                                for c5 in Alfabeto:
                                    cc=c1+c2+c3+c4+c5
                                    Intento=cc.strip()#strip quita espacios
                                    if Intento==Clave:
                                        print('Clave encontrada: ',Intento)
                                        break
                            else:
                                break
                    else:
                        break
            else:
                break
    else:
        break

final=time.time()
print('Tiempo consumido: {:5.2f} seg'.format(final-inicio))
                
                