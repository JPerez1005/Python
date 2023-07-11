telefonos={'José':1234,
           'María':3456,
           'Andrés':5678,
           'Lucía':9876}

if 'Lucía' in telefonos:
    print(f'El usuario sí existe')
    print(telefonos['Lucía'])
else:
    print('Esa clave no existe')

telefonos['Jorge']=6543#añadimos nuevo usuario

telefonos['María']=7890#modificamos un usuario

del telefonos['Andrés']#eliminammos un usuario

print(telefonos)#verificamos usuarios