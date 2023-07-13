fd=open('C/C1/Practicas Classroom/7Archivos/mbox-short.txt',
        'r', encoding='utf-8')
for linea in fd:#recorre cada una de las lineas
    line=linea.rstrip()#quita salto de linea
    if '@' in line:#si no está en la linea
        continue
    if not linea.startswith('From:'):
        continue
    print(line,'Enviado [OK]')
        
fd.close()