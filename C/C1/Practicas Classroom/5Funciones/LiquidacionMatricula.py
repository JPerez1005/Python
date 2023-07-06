'''Se tiene una la información sobre 1 estudiante de una institución de
educación para el trabajo, que realizará su proceso de matrícula financiera.
La información que se conoce del estudiante es la siguiente:
•Código
•Nombre
•Programa a académico al cual pertenece, que puede ser o
1:TécnicoenSistemaso
2:TécnicoenDesarrollodevideojuegoso
3:TécnicoenAnimaciónDigital
•IndicadordeBeca,puedeser:o
1:Beca por rendimiento académico. Descuento del 50% sobre el valor matricula. o
2:BecaCultural
–Deportes. 
Descuento del 40%sobre el valor matrículao
3:SinBeca.
También nos suministran el cuadro de valores de matrícula que
depende del programa académico que cursa el estudiante ,así:

Programa academico:
-Tecnico en sistemas: 800k
-Tecnico en desarrollo de videojuegos: 1 palo
-Tecnico en Animación Digital: 1 palo con 200 lukas

Se pide calcular el valor neto a pagar de matrícula para el estudiante e imprimir el nombre y el valor a pagar por matricula.
'''

#Funciones
def LeerInt(msg):
    while True:
        try:
            n=int(input(msg))
            if n<1 or n>5:
                print('Error!! Ingrese un codigo valido...')
                input('digite cualquier tecla para continuar....')
                continue#Para que vuelva y pregunte
            return n#Se sale de todo
        except ValueError:#Para solo numeros
            print('Error!. Ingrese un numero entero valido.')

def LeerString(msg):
    while True:
        try:
            n=(input(msg))
            if n.strip()=='':#que el usuario no digite un valor vacío
                print('Error!! Ingrese un nombre valido...')
                input('digite cualquier tecla para continuar....')
                continue#Para que vuelva y pregunte
            return n#Se sale de todo
        except ValueError as e:
            print('Error!. Ingrese un numero entero valido.', e.message)#nos retorna el error

def LeerProgramaAcademico():
    TS='Técnico en Sistemas'
    TDV='Técnico en Desarrollo de videojuegos'
    TAD='Técnico en Animación Digital'
    print('*****Ingrese un programa Academico*****')
    print('1: ', TS)
    print('2: ', TDV)
    print('3: ', TAD)
    while True:
        try:
            Op=int(input('Digite el numero de su programa academico: '))
            if Op==1:
                ValorM=800000
                print(f'Usted pertenece a {TS} y el Valor de su matricula es: {ValorM}')
                return ValorM
            elif Op==2:
                ValorM=1000000
                print(f'Usted pertenece a {TDV} y el Valor de su matricula es: {ValorM}')
                return ValorM
            elif Op==3:
                ValorM=1200000
                print(f'Usted pertenece a {TAD} y el Valor de su matricula es: {ValorM}')
                return ValorM
            else:
                print('Opcion No valida')
                input('Digite cualquier tecla para continuar...')
                continue
        except ValueError:#Para solo numeros
            print('Error!. Ingrese un numero entero valido.')

def LeerIndBeca():
    BRA='Beca por rendimiento académico. Descuento del 50% sobre el valor matricula.'
    BC='Beca Cultural – Deportes. Descuento del 40% sobre el valor matrícula'
    SB='Sin Beca.'
    print('*****Ingrese una Beca*****')
    print('1: ', BRA)
    print('2: ', BC)
    print('3: ', SB)
    while True:
        try:
            Op=int(input('Digite el numero de su programa academico: '))
            if Op==1:
                Porcentaje=50
                print(f'Usted tiene {BRA}')
                return Porcentaje
            elif Op==2:
                Porcentaje=40
                print(f'Usted tiene {BC}')
                return Porcentaje
            elif Op==3:
                Porcentaje=0
                print(f'Usted tiene {SB}')
                return Porcentaje
            else:
                print('Opcion No valida')
                input('Digite cualquier tecla para continuar...')
                continue
        except ValueError:#Para solo numeros
            print('Error!. Ingrese un numero entero valido.')
            
def CalMatricula(ProgAcad, Beca):
    B=Beca/100
    BT=B*ProgAcad
    Operacion=int(ProgAcad-BT)
    numero_formateado = '{:,}'.format(Operacion)
    # Reemplazar las comas por puntos
    numero_formateado = numero_formateado.replace(',', '.')
    # Devolver la cadena formateada
    print(numero_formateado)
    return numero_formateado


cod =LeerInt('Ingrese el codigo del estudiante: ')
nom=LeerString('Ingrese el nombre del estudiante: ')
ProgAcad=LeerProgramaAcademico()
Beca=LeerIndBeca()

ValNetoPagar=CalMatricula(ProgAcad,Beca)

print('Estudiante: ',nom)
print(f'El valor neto a pagar es: {ValNetoPagar}')#La coma separa por miles
