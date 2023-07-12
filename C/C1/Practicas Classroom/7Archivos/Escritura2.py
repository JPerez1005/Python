import io

fd=open('C/C1/Practicas Classroom/7Archivos/texto2.txt',
        'w')
lst=['Primera Linea\n','Segunda Linea\n']
fd.writelines(lst)
fd.close()