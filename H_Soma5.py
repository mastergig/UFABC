soma = 0
while True:
    try:
        parametro = int(input())
        if parametro == 0:
            break
        soma = soma + parametro
    except EOFError:
        break
print(soma)