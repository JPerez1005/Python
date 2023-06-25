"""Construya un programa tal que encuentre y muestre todos los enteros positivos, comenzando desde el
cero, que satisfacen la siguiente expresión:"""

P=0
Q=0

print('-'*20, 'Resultado','-'*20,'\n')


for P in range(100):
  for Q in range(100):
    if (P**3) + (Q**4) - (2 * (P**2)) < 680:
      op = (P**3) + (Q**4) - (2 * (P**2))
      if op > 0:
        print(f"P = {P}, Q = {Q} Rta=", op)

print('\n\n','-'*20, 'Fin','-'*20,'\n')
