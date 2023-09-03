valorH=int(input("Ingrese el valor de la hora: "))
cantidad_Horas=int(input("Ingrese la cantidad de horas trabajadas: "))

sueldoBruto=valorH*cantidad_Horas
descuento_eps = sueldoBruto * 0.04
descuento_pension = sueldoBruto * 0.04
sueldo_neto=sueldoBruto-(descuento_eps+descuento_pension)

print("\n", "-" * 50)
print(f"El valor del sueldo bruto es de: ${sueldoBruto:,.0f}", "pesos")
print(f"El valor por descuento de la Eps es de: ${descuento_eps:,.0f}", "pesos")
print(f"El valor por descuento de Pension es de: ${descuento_pension:,.0f}", "pesos")
print(f"El valor final del sueldo neto o total es de: ${sueldo_neto:,.0f}", "pesos")