import sys

parametros = sys.stdin.read()
linhas = parametros.splitlines()

for parametro in linhas:
    valores = parametro.split(" ")

    S = valores[0]
    P = int(valores[1])

    print(S[P])