"""La empresa ACME desea calcular el valor de la nómina de un empleado, tanto el sueldo bruto como el
sueldo neto. El sueldo bruto se calcula a partir del valor de la hora y la cantidad de horas trabajadas. A
esto se le descuenta el valor de la EPS que es el 4%, el valor de la Pensión que es el 4%. El sueldo
neto es el sueldo bruto menos los descuentos. Mostrar al final, el valor del sueldo bruto, cada uno de
los descuentos y el valor del sueldo Neto. Para este ejercicio el valor de la hora es $20.000."""

ValorHora=20000
HorasTrabajadas=int(input("Ingrese la cantidad de horas trabajadas: "))
SueldoBruto=ValorHora*HorasTrabajadas
EPS=SueldoBruto*0.04
Pensión=SueldoBruto*0.04
SueldoNeto=SueldoBruto-(EPS+Pensión)

print('-----------RESULTADO------------')
print("El valor del sueldo bruto es: ",SueldoBruto)
print("El valor del descuento EPS es: ",EPS)
print("El valor del descuento Pensión es: ",Pensión)
print("El valor del sueldo neto es: ",SueldoNeto)
print('-----------------Fin------------------')