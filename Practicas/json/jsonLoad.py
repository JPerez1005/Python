import json

with open('servicios.json') as mis_empleados:
    data = json.load(mis_empleados)

    for usuario in data['usuarios']:
        print('full name:', usuario['id_fullname'])