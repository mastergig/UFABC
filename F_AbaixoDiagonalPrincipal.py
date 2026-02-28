import sys

parametros = sys.stdin.read()
linhas = parametros.splitlines()

operacao = linhas[0]
indice = int(linhas[1])

matriz = linhas[2:]

retorno = float(0)
quantidade = 0

for i in range(indice):
    valores = matriz[i].split(" ")
    atual = valores[:i]
    for valor in atual:
        retorno += float(valor)
        quantidade += 1

if operacao == "M":
    retorno = retorno / quantidade

print(f"{retorno:.1f}")