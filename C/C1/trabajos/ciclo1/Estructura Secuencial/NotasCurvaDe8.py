"""Hacer un algoritmo que dado una nota (de 0.0 a 5.0), calcule la curva de 8 de la nueva nota. La curva
de 8 se calcula multiplicando la nota por 0.8 y sumándole 1."""

nota=''

while nota=='' or nota<0 or nota>5:
    nota=float(input('Por favor digite la nota de entre 0 a 5: '))

print(f'La Curva de 8 es: {nota*0.8+1}')