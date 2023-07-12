'''Hacer un programa que sirva para repasar las capitales de los
paises. Y que cumpla con los siguientes requisitos:

Los paises han de salir en orden aleatorio.
Si se falla se muestra la capital del pais para aprenderla.
Al final del repaso vuelven a salir los paises que se han fallado.
Se seguirá así hasta que se acierten todos.'''

import random

capitales={
    'Canadá': 'Ottawa',
    'Uruguay':'Montevideo',
    'Kenia':'Nairobi',
    'Islandia':'Reikiavik',
    'Filipinas':'Manila'
}

paises=list(capitales.keys())
print('-'*5,'Repasar Capitales','-'*5)
print('-'*30)

while len(paises)>0:
    fallos=[]
    random.shuffle(paises)
    
    for pais in paises:
        print()
        print(f'La capital de {pais} es:')
        
        intento=input('--> ')
        if intento==capitales[pais]:
            print('Has acertado!!')
        else:
            print('¡Era {}!'.format(capitales[pais]))
        
        print()
        input('(enter) para continuar...')
    
    paises=fallos

else:
    print('Has terminado el repaso.')
