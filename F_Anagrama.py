import sys

parametros = sys.stdin.read()
linhas = parametros.splitlines()

p1 = linhas[0]
pc = p1[::-1]
N = int(linhas[1])
lista = linhas[2:2+N]

retorno = "sim" if pc in lista else "nao"

print(retorno)
