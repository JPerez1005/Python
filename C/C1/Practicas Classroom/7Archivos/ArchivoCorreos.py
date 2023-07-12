import io
fd2=open('C/C1/Practicas Classroom/7Archivos/ArchivoCorreos.txt',
        'w')
emails=set()

for x in fd2:
    if x.startswith('From:'):
        x=x[6:]
        emails.add(x)
enviar=list(emails)
envio2=[]
for i in range(len(enviar)-1, 0 , -1):
    x=enviar[i]
    envio=x.rstrip(),'\tenviado OK'
    envio2.append(envio)
    fd2.writelines(envio2)
fd2.close()
