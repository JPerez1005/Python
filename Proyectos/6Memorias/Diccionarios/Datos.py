agenda={
    'Jorge':{
        'Teléfono': 111111,
        'País': 'Ecuador',
        'Personal':{
            'Afición':'Fútbol',
            'Estudios':'Agronomía',
            'Música': 'Clásica'
        }
    },
    'María':{
        'Teléfono': 222222,
        'País': 'Colombia',
        'Personal':{
            'Afición':'Astronomía',
            'Estudios':'Informática',
            'Música': 'Rock'
        }
    },
    'Tomás':{
        'Teléfono': 333333,
        'País': 'España',
        'Personal':{
            'Afición':'Cine',
            'Estudios':'Informática',
            'Música': 'Pop'
        }
    },
    'Carla':{
        'Teléfono': 444444,
        'País': 'México',
        'Personal':{
            'Afición':'Ajedrez',
            'Estudios':'Agronomía',
            'Música': 'Clásica'
        }
    }
}

for nombre,datos in agenda.items():
    print('{}: {}'.format(nombre,datos['País']))