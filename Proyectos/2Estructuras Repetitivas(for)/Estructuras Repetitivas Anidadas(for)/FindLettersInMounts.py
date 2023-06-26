"""Tenemos una tupla con los meses del año
El usuario tiene que digitar una letra para
saber que letra se encuentra en esos mese"""

Mounths=('Enero','Febrero','Marzo','Abril','Mayo',
         'Junio','Julio','Agosto','Septiembre',
         'Octubre','Noviembre','Diciembre')
Letter=input('Digite una letra: ')
for Words in Mounths:
    cont=0
    for Letters in Words.lower():
        if Letters==Letter:
            cont=cont+1
            if cont==1:
                print(f'La letra {Letter} está en el mes de {Words}')
            elif cont>1:
                print(f'La letra {Letter} se repite {cont} veces')