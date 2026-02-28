parametro = input().split()

n = int(parametro[0])
m = int(parametro[1])

matriz = []
for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

menor = 999999999

for j in range(m):
    soma = 0
    for i in range(n):
        soma = soma + matriz[i][j]
    
    if soma < menor:
        menor = soma

print(menor)
