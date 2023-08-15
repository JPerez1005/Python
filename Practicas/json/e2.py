''''''
import json

with open('Ahorradores.json') as clientes:
    data = json.load(clientes)

def cuentas(data):
    cont=0
    datos={}
    datos['clients']=[]
    for usuario in data['cliente']:
        if usuario['Saldo']>35000000:
            cont+=1
            
            datos['clients'].append({
                'consecutivo':cont,
                'numero_cuenta': usuario['NumCuenta'],
                'saldo':usuario['Saldo']
            })
            with open('Dian.json', 'w') as archivo:
                json.dump(datos, archivo, indent=4)

cuentas(data)