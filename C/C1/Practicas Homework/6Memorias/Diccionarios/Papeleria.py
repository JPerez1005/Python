'''INTRODUCCIÓN
Resuelva los siguientes enunciados en Python validando la entrada del usuario y usando diccionarios.
ENUNCIADO
Se realiza la compra de N artí culos, en donde se ingresa el co digo del artí culo y la cantidad y mediante el uso
de diccionarios para los nombres y valores unitarios de los artí culos, el programa debe obtener el nombre
de cada artí culo, cantidad comprada, valor unitario, valor total de acuerdo con la cantidad comprada y
finalmente calcular el valor total de la compra.
Se suministra el diccionario de nombres de artí culo y otro con los valores unitarios.
articulos = {1:"Lapiz",2:"Cuadernos",3:"Borrador",4:"Calculadora",5:"Escuadra"}
valores = {1:2500,2:3800,3:1200,4:35000,5:3700}'''

articulos = {1: "Lapiz", 2: "Cuadernos", 3: "Borrador", 4: "Calculadora", 5: "Escuadra"}
valores = {1: 2500, 2: 3800, 3: 1200, 4: 35000, 5: 3700}

def realizar_compra():
    cantidad_articulos = int(input("Ingrese la cantidad de artículos a comprar: "))

    compra = {}

    for _ in range(cantidad_articulos):
        codigo = int(input("Ingrese el código del artículo: "))
        cantidad = int(input("Ingrese la cantidad comprada: "))

        nombre = articulos.get(codigo)
        valor_unitario = valores.get(codigo)
        valor_total = valor_unitario * cantidad

        compra[nombre] = {
            "Cantidad": cantidad,
            "Valor Unitario": valor_unitario,
            "Valor Total": valor_total
        }

    total_compra = sum(item["Valor Total"] for item in compra.values())

    print("DETALLE DE LA COMPRA")
    for nombre, detalles in compra.items():
        print("Artículo:", nombre)
        print("Cantidad:", detalles["Cantidad"])
        print("Valor Unitario:", detalles["Valor Unitario"])
        print("Valor Total:", detalles["Valor Total"])
        print("------------------")

    print("Total de la compra:", total_compra)


# Ejecutar la función para realizar la compra
realizar_compra()
