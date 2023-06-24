""" Sobre un estudiante conocemos las calificaciones parciales obtenidas en los retos, nota reto 1, nota
reto 2, nota reto 3 y nota de inglés y el nombre del estudiante. Si los porcentajes para cada reto e
inglés son 20%, 25%, 35% y 20% respectivamente, calcular su calificación definitiva e imprimirla,
además del nombre"""

print('----SISTEMA DE NOTAS DE ESTUDIANTES----')

Nombre = input('Digite su nombre: ')

while Nombre == '' or not Nombre.replace(' ', '').isalpha() or len(Nombre)<=2:
    print('No has ingresado ningún nombre o ingresaste caracteres no válidos.\nRecuerde tambien que el numero de caracteres tiene que ser mayor de tres\nIntenta nuevamente.')
    Nombre = input("Ingresa tu nombre: ")

Nota1 = float(input('Ingrese la nota del reto 1: '))
Nota2 = float(input('Ingrese la nota del reto 2: '))
Nota3 = float(input('Ingrese la nota del reto 3: '))
Nota4 = float(input('Ingrese la nota de inglés: '))

Definitiva= (Nota1*0.2)+(Nota2*0.25)+(Nota3*0.35)+(Nota4*0.2)

print(Nombre,'la calificación definitiva es: ',round(Definitiva,2),'\n',Nombre,'Gracias por usar este sistema!!')
print('-----------------Fin------------------')