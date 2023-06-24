#a.	Dada una lista de tuplas, donde cada tupla representa un estudiante con su nombre y su nota en un examen, encontrar  el nombre del estudiante con la nota más alta.
actual=0
estudiantes = [("Juan", 80), ("Ana", 90), ("Pedro", 75), ("Lucía", 95)]

nombre_max_nota = ""
nota_maxima = 0

for estudiante in estudiantes:
    nombre = estudiante[0]#leemos las columnas de cero
    nota = estudiante[1]#leemos las columnas de uno
    
    if nota > nota_maxima:#si una nota actual supera la maxima entonces esta se convertira en la maxima ahora
        nombre_max_nota = nombre
        nota_maxima = nota

print("El estudiante con la nota más alta es:", nombre_max_nota)
