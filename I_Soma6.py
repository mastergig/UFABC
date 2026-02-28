
parametros = input().split()
soma = 0
for parametro in parametros:
    numero = int(parametro) 
    if numero == 0:
      break   
    soma = soma + numero


print(soma)