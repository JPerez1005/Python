empleados = {
    1: {"id": 1, "nombre": "Juan", "horas_trabajadas": 40, "valor_hora": 10000},
    2: {"id": 2, "nombre": "María", "horas_trabajadas": 35, "valor_hora": 12000},
    3: {"id": 3, "nombre": "Pedro", "horas_trabajadas": 45, "valor_hora": 9000},
    4: {"id": 4, "nombre": "Ana", "horas_trabajadas": 50, "valor_hora": 11000},
    5: {"id": 5, "nombre": "Luis", "horas_trabajadas": 42, "valor_hora": 9500},
    6: {"id": 6, "nombre": "Laura", "horas_trabajadas": 38, "valor_hora": 10500},
    7: {"id": 7, "nombre": "Carlos", "horas_trabajadas": 48, "valor_hora": 11500},
    8: {"id": 8, "nombre": "Sofía", "horas_trabajadas": 41, "valor_hora": 9800},
    9: {"id": 9, "nombre": "David", "horas_trabajadas": 37, "valor_hora": 10800},
    10: {"id": 10, "nombre": "Julia", "horas_trabajadas": 44, "valor_hora": 9300},
    # Más Empleados y mas
}

# Tamaño de la página
tamano_pagina = 5

# Obtener la cantidad total de empleados
total_empleados = len(empleados)

# Calcular la cantidad de páginas
total_paginas = (total_empleados + tamano_pagina - 1) // tamano_pagina

# Mostrar las páginas una por una
for pagina in range(total_paginas):
    inicio = pagina * tamano_pagina
    fin = (pagina + 1) * tamano_pagina
    pagina_empleados = list(empleados.values())[inicio:fin]
    
    # Mostrar los empleados de la página actual
    for empleado in pagina_empleados:
        print(f"ID: {empleado['id']}")
        print(f"Nombre: {empleado['nombre']}")
        print(f"Horas trabajadas: {empleado['horas_trabajadas']}")
        print(f"Valor de la hora: {empleado['valor_hora']}")
        print()
    
    # Preguntar al usuario si desea ver la siguiente página o volver al menú
    respuesta = input("Presione Enter para ver la siguiente página o 'm' para volver al menú: ")
    if respuesta.lower() == 'm':
        break  # Salir del bucle si el usuario desea volver al menú
