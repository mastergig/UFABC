n = int(input())
m = int(input())

matriz = []
for i in range(n):
    parametro = list(map(int, input().split()))
    matriz.append(parametro)

for j in range(m):
    for i in range(n):
        if i < n - 1:
            print(matriz[i][j], end=" ")
        else:
            print(matriz[i][j])