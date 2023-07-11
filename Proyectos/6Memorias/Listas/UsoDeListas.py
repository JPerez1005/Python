nombres=['susana','ruben','clara','jorge']
edades=[18,19,20,21]

amigos=[['susana',18],
        ['ruben',19],
        ['clara',20],
        ['jorge',21]]#se uso listas dentro de una lista principal

amigos.append(['sara'])#a la lista principal le añadimos una persona mas

amigos[4].append(22)#tambien le añadimos una edad e indicamos donde

for amigo in amigos:#Mostramos lasa listas dentro de la lista principal
    print('{}: {}'.format(amigo[0],amigo[1]))