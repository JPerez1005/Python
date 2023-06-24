"""Escribir un programa en el que a partir de 
una fecha introducida por teclado con el formato DIA-
MES-AÑO, se obtenga la fecha del día siguiente.

Para realizar el cálculo de forma correcta se debe tener 
en cuenta que hay meses con 30 días y otros
con 31 y que febrero puede tener 29 si es bisiesto el año."""

Dia=int(input('Digite un día: '))
Mes=int(input('Digite un mes: '))
Anio=int(input('Digite un año: '))
print('')
print(f'La Fecha Ingresada fue: {Dia}/{Mes}/{Anio}\n')

if Dia<32 and Mes!=2:
    if Dia<=30 and (Mes==11 or Mes==9 or Mes==4 or Mes==6):
        if Dia<30:
            Dia=Dia+1
        elif Dia==30:
            Dia=Dia-29
            Mes=Mes+1
    elif Dia<=31 and Mes!=11 or Mes!=9 or Mes!=4 or Mes!=6 or Mes!=2:
        if Dia<31:
            Dia=Dia+1
        elif Dia==31 and Mes==12:
            Dia=Dia-30
            Mes=Mes-11
            Anio=Anio+1
        elif Dia==31 and Mes!=12:
            Dia=Dia-30
            Mes=Mes+1
    
    
    #-------------------------RESULTADO----------------------------------------#
    print('-'*10, 'Resultado','-'*10,'\n')
    print(f'La nueva Fecha es: {Dia}/{Mes}/{Anio}\n')
    print('-'*10, 'Fin','-'*10,'\n')

elif Dia<30 and Mes==2:
    if Anio%4==0:
        print('Es bisiesto')
        if Dia==29:
            Dia=1
            Mes=Mes+1
        elif Dia<29:
          Dia=Dia+1
    elif Anio%100==0:
        if Anio%400==0:
            print('Es bisiesto')
            if Dia==29:
                Dia=1
                Mes=Mes+1
            elif Dia<29:
                Dia=Dia+1
        else:
            print('No es bisiesto')
            if Dia==28:
                Dia=1
                Mes=Mes+1
            elif Dia<28:
                Dia=Dia+1
    else:
        print('No es bisiesto')
        if Dia==28:
            Dia=1
            Mes=Mes+1
        elif Dia<28:
            Dia=Dia+1
    
    #-------------------------RESULTADO----------------------------------------#
    print('-'*10, 'Resultado','-'*10,'\n')
    print(f'La nueva Fecha es: {Dia}/{Mes}/{Anio}\n')
    print('-'*10, 'Fin','-'*10,'\n')
else:
    print('Ingreso un Día no valido')