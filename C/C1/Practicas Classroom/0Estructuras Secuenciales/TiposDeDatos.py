num1=10
print(type(num1))
num2=1.25468
print(num2)
sNombre="Oscar"
num2="Daniel"
sw=False
num2=num1//2
num2=num2**2*3-2
print(type(num2))

#OPERADORES DE CADENA
"""COMENTARIOS DE MULTIPLES LINEAS"""

str1="hola"
str2="mundo"
str3=str1+" "+str2
print(str3)

#OPERADOR DE REPETICION
str3=str1*3
print(str3)

#FORMATEO DE CADENAS
#cadenas de tipo f-string
print(f'hola {str2}, {num2}')

#cadenas con formato//heredado de python2
print('Hola %s , %d , %s' % ('mundo',num2,True))