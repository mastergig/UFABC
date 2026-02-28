import sys

parametros = sys.stdin.read()
linhas = parametros.splitlines()

primeira = linhas[0].split(" ")
segunda = linhas[1].split(" ")
terceira = linhas[2].split(" ")

falta = 0

for carimbada in segunda:
    if carimbada not in terceira:
        falta += 1

print(falta)