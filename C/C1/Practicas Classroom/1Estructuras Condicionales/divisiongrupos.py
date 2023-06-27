""" Los alumnos de un curso se han dividido en dos grupos A y B
 de acuerdo al sexo y el nombre. El grupo A esta formado por las
  mujeres con un nombre anterior a la M y los hombres con un 
  nombre posterior a la N y el grupo B por el resto. 
  Escribir un programa que pregunte al usuario su nombre y sexo, 
  y muestre por pantalla el grupo que le corresponde. """

sexo=input('Digite su sexualidad f/m :')
nombre=input('Digite su nombre: ')

if sexo=='f' and nombre<'m':
    print('perteneces al grupo a')
elif sexo=='m' and nombre>'n':
    print('perteneces al grupo a')
else:
    print('perteneces al grupo b')