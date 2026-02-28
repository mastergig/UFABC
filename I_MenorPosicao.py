import sys

parametros = sys.stdin.read()
linhas = parametros.splitlines()

menor = sys.maxsize
posicao = 0
indice = 0

maximo = int(linhas[0])
parametro = linhas[1].split(" ")

for numero in parametro:
    n = int(numero)
    if(menor > n):
        menor = n
        posicao = indice
    indice+=1
    if(indice >= maximo):
        break

print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")