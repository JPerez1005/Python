"""Solicitar al usuario que ingrese una frase y 
luego imprimir un listado de las vocales que 
aparecen en esa frase (sin repetirlas)."""

frase=input('Ingrese una frase: ')

a, e, i, o, u='','','','',''

for letra in frase:
    if letra=='a':
        a='a'
    elif letra=='e':
        e='e'
    elif letra=='i':
        i='i'
    elif letra=='o':
        o='o'
    elif letra=='u':
        u='u'

print(a,e,i,o,u)