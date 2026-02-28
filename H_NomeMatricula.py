import sys

parametros = sys.stdin.read()
linhas  = parametros.splitlines()

for parametro in linhas:
    nome = ""
    matricula = ""
    entrada = parametro.strip()
    for char in entrada:
        if char.isalpha():
            nome+=char
        elif char.isdigit():
            matricula+=char
    print(f"{nome} {matricula}")