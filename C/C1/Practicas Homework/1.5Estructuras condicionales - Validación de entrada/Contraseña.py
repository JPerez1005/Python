"""Hacer un programa que pida al usuario un texto como contraseña y el programa debe validar si es válida.
Una contraseña es válida si:
• Tiene una longitud mínima de 8 caracteres
• Debe contener una letra en minúscula
• Debe contener una letra en mayúscula
• Debe contener un número
• No puede contener espacios
• Debe tener por lo menos uno de los siguientes caracteres especiales (%^&)"""
import string
while True:
    Clave=input('Digite una Contraseña: ')
    if len(Clave)>8:
        """if Clave.find('%')==True or Clave.find('^')==True or Clave.find('&')==True:
            print('La clave contiene valores alfanumericos no validos')
        else:"""
        if (Clave.isalnum()==True):
            if Clave.strip()==Clave:
                print('La clave es valida')
                break
            elif Clave.strip()!=Clave:
                print('La clave no debe tener espacios')
        elif Clave.isalnum()!=True:
            print('La clave no tiene mayusculas o minusculas, o no tiene numeros')
    else:
        print('Digite numeros mayores a 8(esto debido a que es posible que le descifren la clave)')