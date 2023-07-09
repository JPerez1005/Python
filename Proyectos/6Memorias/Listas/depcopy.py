from copy import deepcopy

f=[1,[2,[3,4,5]]]

g=deepcopy(f)#se hace una copia de la lista

f[1][1][1]=5

print(g)
print(f)