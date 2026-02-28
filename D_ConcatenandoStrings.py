import sys

parametros = sys.stdin.read()
linhas  = parametros.splitlines()

for parametro in linhas:
    texto = parametro.replace(" ","")
    
    print(texto)