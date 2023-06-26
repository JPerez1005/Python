""" Dado el nombre y salario de un emnpleado, calcular el
subsidio de transporte, teniendo en cuenta que si el salario es
menor o igual a $1.2000.000 entonces tiene derecho a
un subsidio de transporte por valor de  120.000
de lo contrario no tiene derecho al subsidio de transporte
Se debe visualizar el nombre, salario y subsidio de transporte
"""

nom= input('digite el nombre: ')
sal=int(input('Digite el salario: '))

subtrans = 0
if sal <= 1_200_00:
    subtrans=120_000
else:
    subtrans=0

print('\n', '-'*30)
print('nombre: ',nom)
print('Salario: ',sal)
print('subsidio: ', subtrans)
print('-'*30,'\n')