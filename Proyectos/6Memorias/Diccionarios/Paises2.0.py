'''Programa que guarda un registro de todas
las busquedas que se realizan en un diccionario
, tanto de los elementos que están como de los
que no están.'''

prefijos={
    'COLOMBIA':57,
    'ARGENTINA':54,
    'PERÚ':51,
    'MÉXICO':52,
    'BOLIVIA':591,
    'CHILE':56,
    'ESPAÑA':34,
    'ECUADOR':593
}

busquedas={}
titulo='Prefijos internacionales'
print(titulo.center(40))
print('-'*40)

while True:
    pais=input('País ("q" salir): ').upper()
    if pais=='Q':
        break
    prefijo=prefijos.get(pais,'No disponible')

    print()
    print('{}: {}'.format(pais, prefijo))
    print()

    busquedas.setdefault(pais,0)
    busquedas[pais]+=1

    print('-'*40)
    print('Registro de busquedas:')
    for k,v in busquedas.items():
        print('{}: {}'.format(k,v))
    print('-'*40)