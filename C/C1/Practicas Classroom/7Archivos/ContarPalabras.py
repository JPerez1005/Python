import io

fd=open('C/C1/Practicas Classroom/7Archivos/mbox-short.txt',
        'r', encoding='utf-8')
cont=0
for linea in fd:#recorre cada una de las lineas
    if linea.lower().count('subject:'):
        #si inicia con from la linea entonces...
        cont+=1
        
fd.close()

print('Cantidad de lineas que tienen from: ',cont)
