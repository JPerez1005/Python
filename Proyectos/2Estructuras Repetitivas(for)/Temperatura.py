"""Ingresar temperaturas, hay que comprobar
que todas las temperaturas esten entre 18 y
25 incluidos. Si alguna no cumple la condición
se para el programa y lo indica, si no va
mostrando que la temperatura verificada es
correcta."""

salir=''
for Num in range(1,101):
    No=int(input('Digite una temperatura: '))
    if No>17 and No<26:
        print('La temperatura es valida')
    else:
        print('La temperatura no es la indicada')
    salir=input('Para salir escriba "salir" tal cual: ')
    if salir.lower()=='salir':
        print('Saliendo...')
        break