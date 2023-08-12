import os
os.system('clear')

def promedio(listaVentas):
    return 2.5

misDatos=open('/home/spukN01-078/Documents/julian/Python/C/C1/Practicas Classroom/7Archivos/archivos/datos.txt','r+')
#Abrimos el archivo

unaLinea=misDatos.readline()#Del archivo leemos la linea

lineas_actualizadas=[]#Creamos una lista

while unaLinea:#mientras una linea exista entonces....
    #print(unaLinea)
    listaActualizada=[]#creamos otra lista
    lista=unaLinea.strip().split(',')
    mes=lista[0]
    ventasMes=[int(valor) for valor in lista[1:]]
    #print(mes,ventasMes)
    prom=promedio(ventasMes)
    linea_actualizada=f"{unaLinea.strip()} ** {prom:.2f} \n"
    lineas_actualizadas.append(linea_actualizada)
    #print(linea_actualizada)
    
    unaLinea=misDatos.readline()

#print(lineas_actualizadas)

misDatos.close()

misDatos=open('/home/spukN01-078/Documents/julian/Python/C/C1/Practicas Classroom/7Archivos/archivos/datos.txt','w')
for linea in lineas_actualizadas:
    misDatos.write(linea)
misDatos.close()