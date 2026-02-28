import sys

parametros = sys.stdin.read()
linhas = parametros.splitlines()

vetor = linhas[1].split(" ")
busca = linhas[3:]

for item in busca:
    try:
        indice = vetor.index(item)
        print(indice)
    except ValueError:
        print("-1")