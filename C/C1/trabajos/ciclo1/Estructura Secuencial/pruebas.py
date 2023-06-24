final = 0
cont=0
while cont<4:
    nota = float(input("Ingresa una nota: "))
    if cont==1:
        nota=nota*0.2

    if cont==4:
        nota=nota*0.2
    
    if cont==2:
        nota=nota*0.25
    
    if cont==3:
        nota=nota*0.35
    
    final = final + nota
    cont+=1


print("Nota final:", final)
