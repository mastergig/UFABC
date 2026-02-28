import sys

parametros = sys.stdin.read()
linhas = parametros.splitlines()

for parametro in linhas:

    valores = parametro.split(" ")

    S1 = valores[0]
    S2 = valores[1]

    retorno =  "iguais" if S1 == S2 else "diferentes"

    print(retorno)