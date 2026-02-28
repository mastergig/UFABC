import sys

parametros = sys.stdin.read()
linhas = parametros.splitlines()

for parametro in linhas:
    texto = parametro

    tamanho = len(texto)

    print(tamanho)