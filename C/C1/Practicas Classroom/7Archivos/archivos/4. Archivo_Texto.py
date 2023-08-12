'''Crear archivo que lea separe y saque promedio'''

meses = "Datos.txt"

def verificar():
    # Verificar si el archivo existe
    try:
        with open(meses, "r"):
            print("El archivo de meses existe.")
    except FileNotFoundError:
        print("El archivo de empleados no existe. Se creará uno nuevo.")
