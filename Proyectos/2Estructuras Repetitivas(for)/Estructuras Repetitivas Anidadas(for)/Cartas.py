"""Crea una baraja con bucles añadiendo
las cartas a una lista mediante bucles for"""

Tantos=['A','1','2','3','4','5','6','7','S','C','R']

Palos=['oros','copas','espadas','bastos']

Baraja=[]

#carta='{} de {}'.format(t,p)

for t in Tantos:
    for p in Palos:
        carta='{} de {}'.format(t,p)
        Baraja.append(carta)
    

for i in range(0,40,4):
    print('{} {} {} {}'.format(Baraja[i],Baraja[i+1],Baraja[i+2],Baraja[i+3]))