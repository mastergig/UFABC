import sys

parametros = sys.stdin.read()
linhas  = parametros.splitlines()

maximo = linhas[0]
valores = linhas[1].split(" ")
retorno = ""
contagem = 0

for valor in valores:
    numero = int(valor)
    if(numero % 2 == 0):
        retorno += f"{numero} "
        contagem += 1

print(f"{retorno}{contagem}")