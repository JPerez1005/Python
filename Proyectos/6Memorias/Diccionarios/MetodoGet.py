inventario={
    'Tornillos': 100,
    'Tuercas': 150,
    'Arandelas': 250
}

articulo=input('Articulo: ')

numero=inventario.get(articulo, 0)#nos devuelve el valor del articulo

print('{}: {}'.format(articulo, numero))