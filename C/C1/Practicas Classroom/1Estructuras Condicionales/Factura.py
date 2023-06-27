"""Se trata de escribir el algoritmo que permita emitir la factura correspondiente a una compra de un
artículo determinado, del que se adquieren una o varias unidades. El IVA por aplicar es del 15 por
100 y si el precio bruto (precio venta más IVA) es mayor de 1.000 euros, se debe realizar un
descuento del 5 por 100."""

compra=int(input('Digite el valor del articulo: '))
narticulos=int(input('Digite el numero de articulos a comprar: '))

IVA=compra*0.15

preciobruto=compra+IVA*narticulos


if preciobruto>1000:
    preciobruto=preciobruto*0.05
    print('Se hizo un descuento del 5%')
print('-'*5,'Factura','-'*5,'\n')
print('El valor del Producto es: ',compra)
print('Cantidad de articulos: ',narticulos)
print('El precio total es: ',preciobruto,'\n')
print('-'*5,'fin','-'*5,'\n')