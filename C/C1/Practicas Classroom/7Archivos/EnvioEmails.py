import io

fd=open('C/C1/Practicas Classroom/7Archivos/mbox-short.txt',
        'r', encoding='utf-8')

emails=set()

for x in fd:
    if x.startswith('From:'):
        x=x[6:]
        emails.add(x)
enviar=list(emails)
for i in range(len(enviar)-1, 0 , -1):
    x=enviar[i]
    print(x.rstrip(),'\tenviado OK')
fd.close()