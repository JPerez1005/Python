"""Escriba un programa que reciba un número entero positivo
 y muestre en pantalla la cantidad de dígitos que este tiene.
No puede convertir el número a cadena, ni usar funciones de cadena.
 Solo operadores aritméticos."""

Num = int(input("Ingrese un número entero positivo: "))
Digitos=1
if Num>9:
    Digitos=2
    if Num>99:
        Digitos=3
        if Num>999:
            Digitos=4
            if Num>9999:
                Digitos=5
                if Num>99999:
                    Digitos=6
                else:
                    Digitos=7

print('-'*10, 'Resultado','-'*10,'\n')
if Num<10:
    print(f'El numero solo tiene {Digitos} Digito')
elif Num<1000000:
    print(f'El numero tiene {Digitos} Digitos')
else:
    print(f'El numero tiene más de {Digitos} Digitos')
print('-'*10, 'Fin','-'*10,'\n')