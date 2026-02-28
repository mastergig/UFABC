n = int(input())

matriz = []
for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

superior = True
inferior = True

for i in range(n):
    for j in range(n):
        if i > j and matriz[i][j] != 0:
            superior = False
        if i < j and matriz[i][j] != 0:
            inferior = False

if superior and inferior:
    print("SIM: DIAGONAL")
elif superior:
    print("SIM: SUPERIOR")
elif inferior:
    print("SIM: INFERIOR")
else:
    print("NAO")
