"""Los telefonos de una empresa tienen el siguiente
formato prefijo-numero-extension donde el prefijo
es el codigo del pais +34, y la extensión tiene
dos digitos (por ejemplo +34-913724710-56).
Escribir un programa que pregunte por un numero
de telefono con este formato y muestre por 
pantalla el numero de telefono sin el prefijo
y la extension"""

print('Por favor digite un numero con el siguiente formato:\n\
      +34-913724710-56')
Num=input('Digite el numero: ')
EstaBien=False
EstaBien2=False
while True:
    if Num.find('+')==0:
        print('si aparece de primeras')
        if Num.find('-')==3 and Num.rfind('-')==13:
            print('esta bien')
            EstaBien=True
        else:
            print('Tiene un mal formato')
            break
    else:
        print('No aparece el signo +, como primer digito')
        break
    if any(char.isalpha() for char in Num):
    #if any(char.isdigit() for char in Num):#es para cuando hay numeros
        print('No se admiten letras')
        break
    else:
        print('esta bien')
        EstaBien2=True
        break

if EstaBien==True and EstaBien2==True:
    print('El formato es valido')
else:
    print('Algo salio mal')