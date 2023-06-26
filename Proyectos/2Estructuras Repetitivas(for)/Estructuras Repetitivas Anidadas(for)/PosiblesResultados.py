"""Cinco amigos van a hacer una carrera:
muestra todos los posibles resultados 
que se puedan dar en esa carrera.
Es decir, el orden en que pueden llegar
a la meta los cinco amigos.

Incluye un contador que compruebe cuantas
posibilidades se dan"""

Amigos=['Tomas','Maria','Laura','Miguel','Carlos']

cont=0

for i in Amigos:
    for j in Amigos:
        for k in Amigos:
            for m in Amigos:
                for n in Amigos:
                    if i!=j and i!=k and i!=m and i!=n and \
                       j!=k and j!=m and j!=n and \
                       k!=m and k!=n and m!=n:
                        Orden=[i,j,k,m,n]
                        cont+=1
                        print('{:3d} : {}'.format(cont, Orden))
    