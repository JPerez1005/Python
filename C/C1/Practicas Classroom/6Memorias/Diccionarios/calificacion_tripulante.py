'''Dada la siguiente información sobre las calificaciones
de estudiantes de una institucion educativa:
-codigo
-nombre
-nota1(peso de 30%)
-nota2(peso de 30%)
-nota3(peso de 40%)
el proceso se termina cuando el codigo que se ingrese
sea 999.(bandera)
se pide calcular:

La nota definitiva de cada estudiante e indicar con un mensaje
si aprobó o reprobó, usando funciones

Para aprobar, la nota debe ser mayor o igual a 3.0 y la
informacion en su totalidad se debe almacenar en 
diccionarios
'''

notas={1:0.3, 2:0.3, 3:0.4}
estudiantes={}
bandera=True

while bandera==True:
    codigo=int(input('Digite el codigo del estudiante: '))
    if codigo==999:
        break
    nombre=input('Digite nombre del estudiante: ')
    nota1=float(input('Ingrese la nota 1:'))
    nota2=float(input('Ingrese la nota 2:'))
    nota3=float(input('Ingrese la nota 3:'))
    estudiantes[codigo]={}
    estudiantes[codigo]['nombre']=[nombre]
    estudiantes[codigo]['nota1']=[nota1]
    estudiantes[codigo]['nota2']=[nota2]
    estudiantes[codigo]['nota3']=[nota3]

print('-'*5,'INFORME','-'*5)
print('='*30)
def calcularNotas():
    for codigos in estudiantes.keys():
        cal1=estudiantes[codigos]['nota1']*notas[1]#multiplico los diccionarios
        cal2=estudiantes[codigos]['nota2']*notas[2]#multiplico los diccionarios
        cal3=estudiantes[codigos]['nota3']*notas[3]#multiplico los diccionarios
        final=cal1+cal2+cal3
        if final>=3:
            nombre_estudiante=estudiantes[codigos]['nombre']
            print(f'El estudiante {nombre_estudiante} aprobó con una nota de {final}')
        else:
            nombre_estudiante=estudiantes[codigos]['nombre']
            print(f'El estudiante {nombre_estudiante} reprobó con una nota de {final}')
        estudiantes[codigos]['final']=[final]
calcularNotas()
print('='*30)