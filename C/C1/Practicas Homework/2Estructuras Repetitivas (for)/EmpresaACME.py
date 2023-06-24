"""La empresa ACME desea calcular el valor de la nómina de N empleados (estos N empleados son
ingresados por el usuario), tanto el sueldo bruto como el sueldo neto. El sueldo bruto se calcula a partir
del valor de la hora y la cantidad de horas trabajadas. A esto se le descuenta el valor de la EPS que es el
4%, el valor de la Pensión que es el 4%. El sueldo neto es el sueldo bruto menos los descuentos. Por
cada empleado se quiere mostrar, el valor del sueldo bruto, cada uno de los descuentos y el valor del
sueldo Neto. Para este ejercicio el valor de la hora es $20.000.
Al final se debe mostrar una estadística con los totales de los salarios brutos, EPS, Pensión y salarios
netos. Luego mostrar el empleado que más gana en salario neto (nombre y salario neto), el empleado
que menos gana en salario neto (nombre y salario neto) y los promedios de sueldos brutos y sueldos
netos."""

NCantidad=int(input('Digite la cantidad de empleados de la empresa: '))
ValorHora=20000
CantidadHoras=0
SBruto=0
SNeto=0
TSBruto=0
TEPS=0
TPension=0
TNeto=0
MayorSueldo=0
MenorSueldo=20000*10
MayorNombre=''
MenorNombre=''
PromedioSBruto=0
PromedioSNeto=0
for i in range(0, NCantidad):
    Nombre=input('Digite el nombre del empleado: ')
    CantidadHoras=int(input('Digite la cantidad de horas: '))
    SBruto=ValorHora*CantidadHoras
    EPS=SBruto*0.04
    Pension=SBruto*0.04
    SNeto=SBruto-(EPS+Pension)
    print('-'*20, f'Factura de {Nombre}','-'*20,'\n')
    print('Nombre: ',Nombre)
    print('Valor del Sueldo Bruto: {:.2f}'.format(SBruto))
    print('Valor del Descuento EPS: {:.2f}'.format(EPS))
    print('Valor del Descuento Pension: {:.2f}'.format(Pension))
    print('Valor del Sueldo Neto: {:.2f}'.format(SNeto))
    print('\n\n','-'*20, f'Fin Factura de {Nombre}','-'*20,'\n')

    TSBruto=TSBruto+SBruto
    TPension=TPension+Pension
    TEPS=TEPS+EPS
    TNeto=TNeto+SNeto
    
    if MayorSueldo<SNeto:
        MayorSueldo=MayorSueldo+SNeto
        MayorNombre=Nombre

    if MenorSueldo>SNeto:
        MenorSueldo=MenorSueldo+SNeto
        MenorNombre=Nombre
    
    PromedioSBruto=round(TSBruto/NCantidad,2)
    PromedioSNeto=round(TNeto/NCantidad,2)

print('\n\n','-'*20, 'Resultado Estadistico','-'*20,'\n')
print(f'Total sueldo bruto: {TSBruto}')
print(f'Total descuento de pension: {TPension}')
print(f'Total descuento de EPS: {TEPS}')
print(f'Total sueldo Neto: {TNeto}\n')
print(f'El empleado con mayor sueldo: {MayorNombre}')
print(f'Con un sueldo de: {MayorSueldo}\n')
print(f'El empleado con menor sueldo: {MenorNombre}')
print(f'Con un sueldo de: {MenorSueldo}\n')
print(f'El promedio total de Salario Bruto es de: {PromedioSBruto}')
print(f'El promedio total de Salario Neto es de: {PromedioSNeto}\n')
print('\n\n','-'*20, 'Fin','-'*20,'\n')