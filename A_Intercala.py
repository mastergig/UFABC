import sys

linhas = sys.stdin.read().splitlines()

q1 = int(linhas[0])
q2 = int(linhas[1])

lista1 = [int(x) for x in linhas[2:2 + q1]]
lista2 = [int(x) for x in linhas[2 + q1:2 + q1 + q2]]

i = 0
j = 0
resultado = []

while i < q1 and j < q2:
    if lista1[i] <= lista2[j]:
        resultado.append(lista1[i])
        i += 1
    else:
        resultado.append(lista2[j])
        j += 1

resultado.extend(lista1[i:])
resultado.extend(lista2[j:])

for n in resultado:
    print(n)