soma = 0

while True:
  try:
    parametro = int(input())
    soma = soma + parametro

  except EOFError:
    break

print(soma)