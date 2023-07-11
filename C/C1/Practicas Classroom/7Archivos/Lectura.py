import io

#abrirlo
fd=open('/home/spukN01-078/julian/Python/C/C1/Practicas Classroom/7Archivos/texto.txt','r', encoding='utf-8')
#Leer
fd.seek(51)
#leer=fd.read()
leer2=fd.readline(6)
leer3=fd.readlines()
#cerrarlo
fd.close()

print(leer2.rstrip())
#print(leer3)