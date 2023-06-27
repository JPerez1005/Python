"""Se ingresan los nombres y notas de estudiantes, 
indique cual es el promedio del curso, cual es el
estudiante con mayor y menor nota (nombre y nota).
El ingreso se termina cuando el profesor ingrese 
FIN en el nombre."""

Final=float('inf')
i=0
NotaSum=0
NotaMayor=float('-inf')
NombreMayor=''
NombreMenor=''
NotaMenor=float('inf')
while i<Final:
    i=i+1
    print('Si quiere salir del programa digite FIN en el ingreso de nombre')
    Nombre=input('Ingrese el nombre del estudiante: ')
    if Nombre=='FIN':
        break
    Nota=float(input('Ingrese nota del estudiante'))
    NotaSum=NotaSum+Nota
    if NotaMayor<Nota:
        NotaMayor=Nota
    if NotaMenor>Nota:
        NotaMenor=Nota
    print('-'*10,f'finalizo la nota del estudiante {Nombre}','-'*10)

NotaProm=NotaSum/i

print('El promedio del salon es: ',NotaProm)
print(f'La nota mayor es de: {NotaMayor} y la tiene {NombreMayor}')
print(f'La nota menor es de: {NotaMenor} y la tiene {NombreMenor}')

print('-'*10,f'FINAL','-'*10)

