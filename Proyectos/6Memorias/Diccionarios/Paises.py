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
nombre=input('Agregue un país: ')
prefijo=prefijos.setdefault(nombre,0)
prefijos[nombre]+=1
# Ordenar las claves del diccionario alfabéticamente
claves_ordenadas = sorted(prefijos.keys())
for clave in claves_ordenadas:
    print(f'{clave}: {prefijos[clave]}')
    print()  # Salto de línea

print()
