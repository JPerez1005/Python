"""Hacer un algoritmo que dado una nota (de 0.0 a 5.0), calcule la curva de 8 de la nueva nota. La curva
de 8 se calcula multiplicando la nota por 0.8 y sumándole 1."""

Nota=''

while Nota=='' or Nota<0 or Nota>5:
    Nota=float(input('Por favor digite la nota de entre 0 a 5: '))

NotaFinal=((Nota*0.8)+1)

print('------------------RESULTADO-------------------\n')
print("La Curva de 8 es: {:.2f}".format(NotaFinal))
print('')