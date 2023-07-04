'''Escribir una función que reciba una cadena que
contiene un largo número entero y devuelva una
cadena con el número y las separaciones de miles.
Por ejemplo, si recibe 1234567890, debe devolver
1.234.567.890.'''

def formatear_numero(cadena):
    # Convertir la cadena en un entero
    numero = int(cadena)
    # Formatear el número con separaciones de miles
    numero_formateado = '{:,}'.format(numero)
    # Reemplazar las comas por puntos
    numero_formateado = numero_formateado.replace(',', '.')
    # Devolver la cadena formateada
    return numero_formateado

cadena=int(input('Digite numeros: '))
numero_formateado = formatear_numero(cadena)
print(numero_formateado)