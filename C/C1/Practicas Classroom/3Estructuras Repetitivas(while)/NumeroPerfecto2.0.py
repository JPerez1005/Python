"""Construya un programa que verifique si un número dado es perfecto. 
Un número perfecto es un número entero positivo que es igual a la suma 
de sus divisores propios positivos (excluyendo el número mismo). 
En otras palabras, si sumas todos los divisores propios de un número perfecto, el
resultado será igual al número original.

Por ejemplo, el número 6 es considerado un número perfecto. Sus divisores 
propios son 1, 2 y 3. Si sumamos estos números: 1 + 2 + 3 = 6, obtenemos 
el mismo número original."""



num=int(input('Digite un numero: '))
per=0
i=1
while i<num:
    if num%i==0:
        per=per+i
        print(per)
    i=i+1
print('-'*5,'Resultado','-'*5,'\n')
if per==num:
    print('El numero es perfecto')
else:
    print('el numero no es perfecto')
print('-'*5,'Fin','-'*5,'\n')