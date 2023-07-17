Letra1 = ''#letra 1 uno como variable
Letra2 = ''#letra 2 uno como variable
Redondeo = 1
Validacion = 1
Verda=True
Verda2=True
while Verda==True:
    Palabra = input('Ingrese una cadena: ')
    if Palabra.strip().isalpha():
        Verda=False
    else:
        print('Ingrese solo letras')
NuevoPalabra = Palabra

while Verda2==True:
    for x in NuevoPalabra.lower():
        if Redondeo % 2 != 0:
            Letra1 = x
        elif Redondeo % 2 == 0:
            Letra2 = x
        Redondeo += 1
        if Letra1 == Letra2:
            NuevoPalabra = NuevoPalabra.replace(x,'',2)
            Letra1 = ''
            Letra2 = ''
    Redondeo = 1
    if NuevoPalabra == '':
        NuevoPalabra = 'Cadena Vacia'
        Verda2=False
    if len(NuevoPalabra) == Validacion:
        Verda2=False
    Validacion += 1

print(f'\nLa cadena resultante es: {NuevoPalabra.strip()}\n')