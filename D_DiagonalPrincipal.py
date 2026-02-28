import sys

parametros = sys.stdin.read()
linhas = parametros.splitlines()

operacao = linhas[0]
indice = int(linhas[1])
matriz = linhas[2:]

retorno = float(0)

for i in range(indice):
    atual = matriz[i].split(" ")
    retorno += float(atual[i])

if operacao == "M":
    retorno = retorno / indice

print(f"{retorno:.1f}")