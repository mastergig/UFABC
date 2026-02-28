n = int(input())

matriz = []
for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

triangular = True

for i in range(n):
    for j in range(n):
        if i > j:
            if matriz[i][j] != 0:
                triangular = False

print("SIM" if triangular else "NAO")
