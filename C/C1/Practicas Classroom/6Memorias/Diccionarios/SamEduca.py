'''La institucion educativa SamEduca cuenta con N docentes, conociendo de cada
'''

diccionario_categoria={1:25000, 2:30000, 3:40000, 4: 45000, 5:60000}

total_honorarios=0#aquí colocamos todos los honorarios
docentes={}


while True:
    try:
        cedula=int(input('cedula del docente: '))
        nombre=input('Nombre del docente: ')
        categoria=int(input('Categoria del docente: '))
        horas= int(input('Horas laboradas en el mes por el docente: '))
        docentes[cedula]={}
        docentes[cedula]['nombre']=nombre
        docentes[cedula]['categoria']=categoria
        docentes[cedula]['horas']=horas

        opc=input('Desea Agregar otro docente S/N?: ')
        if opc.lower() == 'n':
            break
    
    except ValueError:
        print('Solo digite numeros')
    
print('-'*5,'INFORME','-'*5)
print('='*30)
for cedulas in docentes.keys():#recorro las llaves del diccionario.keys() recorre las llaves conk
    h=docentes[cedulas]['horas']*diccionario_categoria[docentes[cedulas]['categoria']]#multiplico los diccionarios
    #y los conecto para multiplicar las horas con el valor de la categoria
    total_honorarios+=h#acumulamos el total de honorarios
    print(docentes[cedulas]['nombre'],  f'--${h:,}')
print('='*30)
print(f'Total honorarios de los docentes: ${total_honorarios:,}')