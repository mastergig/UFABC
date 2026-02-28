import sys

parametros = sys.stdin.read()
linhas = parametros.splitlines()

palavras = [linha.strip() for linha in linhas if linha.strip()]

if not palavras:
    print("Nenhuma palavra foi informada")
else:
    maior = max(palavras[::-1], key=len)
    print(f"A maior palavra informada foi {maior}")