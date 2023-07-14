# Importar el módulo
import json
def AsignacionProductos():
    productos={}
    id=input('Digite el id del producto: ')
    nombre=input('Digite el nombre del producto: ')
    cant=input('Digite la cantidad de productos que hay: ')
    valor=input('Digite el valor de producto: ')
    TipoIva=input('Digite el tipo de iva: ')
    if TipoIva=='1':
        TipoIva=0
    elif TipoIva=='2':
        TipoIva=0.05
    elif TipoIva=='3':
        TipoIva=0.19
    productos[id] = {
            'id':id,
            "producto": nombre,
            "cantidad": cant,
            "valor": valor,
            "Tipo de Iva": TipoIva
        }
    with open('Acme.json','a+') as archivo:
        json.dump(productos, archivo)
        archivo.write('\n')


cliente = {
    "Codigo del Producto": "Nora",
    "Valor del producto": 56,
    "Cantidad comprada": "45355",
    "Tipo Iva": "verdes",
    "usa_lentes": False
}

AsignacionProductos()