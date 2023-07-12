import io

fd=open('C/C1/Practicas Classroom/7Archivos/mbox-short.txt',
        'r', encoding='utf-8')
cont=0
for linea in fd:#recorre cada una de las lineas
    line=linea.rstrip()#quita salto de linea
    if not '@uct.ac.za' in line:
        continue
    print(line)
        
fd.close()

