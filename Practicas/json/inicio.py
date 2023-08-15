import json

data={}
data['clients']=[]

data['clients'].append({
    'firts_name':'Theodoric',
    'last_name':'rivers',
    'age':36,
    'amounth':1.11
})

data['clients'].append({
    'firts_name':'Julian',
    'last_name':'Perez',
    'age':22,
    'amounth':500000
})

with open('data.json','w') as file:
    json.dump(data,file,indent=4)

print(data)
