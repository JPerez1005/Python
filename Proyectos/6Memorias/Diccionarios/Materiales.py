materiales={
    'cuadernos':5,
    'bolígrafos':7,
    'reglas':3,
    'borradores':4
}

articulo=input('Artículo: ')
unidades=materiales.setdefault(articulo,0)#nos devuelve el numero de unidades de ese articulo


print('Hay {} unidades de {}'.format(unidades, articulo))
