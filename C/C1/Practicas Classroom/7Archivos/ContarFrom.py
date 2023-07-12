import io

fd=open('C/C1/Practicas Classroom/7Archivos/mbox-short.txt',
        'r', encoding='utf-8')
cont=0
for linea in fd:#recorre cada una de las lineas
    if linea.startswith('From'):
        #si inicia con from la linea entonces...
        cont+=1
        
fd.close()

print('Cantidad de lineas que empiezan con from: ',cont)
