import sys

parametros = sys.stdin.read()
linhas  = parametros.splitlines()

maximo = linhas[0]
valores = linhas[1].split(" ")
retorno = ""
indice = 0
contagem = 0

for valor in valores:
    numero = int(valor)
    if(indice % 2 == 0):
        retorno += f"{numero} "
    if(numero % 2 == 0):
        contagem += 1
    indice+= 1
        
print(f"{retorno}{contagem}")