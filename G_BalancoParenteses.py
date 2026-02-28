parametros = input().strip()
parentese = 0

for caractere in parametros:
    if(caractere == "("):
        parentese+=1
    elif(caractere == ")"):
        parentese-=1
    if(parentese<0):
        break
print("correct" if parentese == 0 else "incorrect")