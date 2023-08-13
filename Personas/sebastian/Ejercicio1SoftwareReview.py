import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_nota_definitiva(notas_parciales):
    return round(sum(notas_parciales) / len(notas_parciales), 2)

def validar_nota(nota):
    try:
        nota = float(nota)
        if 0.0 <= nota <= 5.0:
            return True
        else:
            print("La nota debe estar entre 0.0 y 5.0")
            return False
    except ValueError:
        print("Ingrese una nota válida.")
        return False

def agregar_estudiante(estudiantes):
    codigo = input("Ingrese el código del estudiante: ")
    nombre = input("Ingrese el nombre completo del estudiante: ")
    notas_parciales = []
    for i in range(3):
        while True:
            nota = input(f"Ingrese la nota parcial {i+1}: ")
            if validar_nota(nota):
                notas_parciales.append(float(nota))
                break

    estudiantes[codigo] = {
        "nombre": nombre,
        "notas_parciales": notas_parciales,
        "nota_definitiva": calcular_nota_definitiva(notas_parciales)
    }
    print("Registro agregado exitosamente.")

def buscar_estudiante(estudiantes):
    codigo_buscar = input("Ingrese el código del estudiante a buscar: ")
    if codigo_buscar in estudiantes:
        estudiante = estudiantes[codigo_buscar]
        print(f"Código: {codigo_buscar}")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Nota 1: {estudiante['notas_parciales'][0]}")
        print(f"Nota 2: {estudiante['notas_parciales'][1]}")
        print(f"Nota 3: {estudiante['notas_parciales'][2]}")
    else:
        print("Estudiante no encontrado.")

def actualizar_estudiante(estudiantes):
    codigo_actualizar = input("Ingrese el código del estudiante a actualizar: ")
    if codigo_actualizar in estudiantes:
        estudiante = estudiantes[codigo_actualizar]
        print(f"Actualizando datos del estudiante {estudiante['nombre']}")
        nombre = input("Ingrese el nuevo nombre completo del estudiante: ")
        notas_parciales = []
        for i in range(3):
            while True:
                nota = input(f"Ingrese la nueva nota parcial {i+1}: ")
                if validar_nota(nota):
                    notas_parciales.append(float(nota))
                    break

        estudiante["nombre"] = nombre
        estudiante["notas_parciales"] = notas_parciales
        estudiante["nota_definitiva"] = calcular_nota_definitiva(notas_parciales)
        print("Datos actualizados exitosamente.")
    else:
        print("Estudiante no encontrado.")

def borrar_estudiante(estudiantes):
    codigo_borrar = input("Ingrese el código del estudiante a borrar: ")
    if codigo_borrar in estudiantes:
        del estudiantes[codigo_borrar]
        print("Estudiante borrado exitosamente.")
    else:
        print("Estudiante no encontrado.")

def calcular_notas_definitivas(estudiantes):
    for estudiante in estudiantes.values():
        estudiante["nota_definitiva"] = calcular_nota_definitiva(estudiante["notas_parciales"])
    print("Notas definitivas calculadas exitosamente.")

def listar_estudiantes(estudiantes):
    clear_screen()
    print("{:^3} {:^20} {:^20} {:^20} {:^20} {:^20}".format("ID", "Nombre", "Nota Parcial 1", "Nota Parcial 2", "Nota Parcial 3", "Nota Definitiva"))
    print("="*118)
    for codigo, estudiante in estudiantes.items():
        nombre = estudiante['nombre']
        nota_parcial1 = estudiante['notas_parciales'][0]
        nota_parcial2 = estudiante['notas_parciales'][1]
        nota_parcial3 = estudiante['notas_parciales'][2]
        nota_definitiva = estudiante['nota_definitiva']
        print("{:^3} {:^20} {:^20} {:^20} {:^20} {:^20}".format(codigo, nombre, nota_parcial1, nota_parcial2, nota_parcial3, nota_definitiva))
    
    promedio_general = sum([estudiante['nota_definitiva'] for estudiante in estudiantes.values()]) / len(estudiantes)
    print("\nPromedio General del Curso: {:.2f}".format(promedio_general))
    
def main():
    estudiantes = {}

    while True:
        clear_screen()
        print("\nMENÚ PRINCIPAL")
        print("1. Agregar un nuevo registro")
        print("2. Buscar un Estudiante")
        print("3. Actualizar datos del Estudiante")
        print("4. Borrar un estudiante")
        print("5. Calcular notas definitivas")
        print("6. Listar estudiantes con notas definitivas y ver promedio general")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_estudiante(estudiantes)
            input("Presione Enter para continuar...")

        elif opcion == "2":
            buscar_estudiante(estudiantes)
            input("Presione Enter para continuar...")

        elif opcion == "3":
            actualizar_estudiante(estudiantes)
            input("Presione Enter para continuar...")

        elif opcion == "4":
            borrar_estudiante(estudiantes)
            input("Presione Enter para continuar...")

        elif opcion == "5":
            calcular_notas_definitivas(estudiantes)
            input("Presione Enter para continuar...")

        elif opcion == "6":
            listar_estudiantes(estudiantes)
            input("Presione Enter para continuar...")

        elif opcion == "7":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            input("Presione Enter para continuar...")

main()
