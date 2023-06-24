pregunta=input('-De cuanto es la temperatura? :')
conversion=int(pregunta)

if conversion<20:
    print('nivel bajo!')
    if conversion<10:
        print('  ...Subnivel azul')
    else:
        print('  ...Subnivel verde')
else:
    print('nivel alto!')
    if conversion<30:
        print('  ...Subnivel naranja')
    else:
        print('  ...Subnivel rojo')