par = 0
imp = 0
pos = 0
neg = 0
# Loop para retornar a quantidade de valores indicado
i = 0
for i in range(5):
    valor = int(input())
# Verifica se o valor é par
    if (valor % 2 == 0):
        par += 1
    else:
        imp += 1
    if (valor > 0):
         pos +=1
    else:
        if (valor < 0):
            neg += 1


print("{} valor(es) par(es)".format(par))
print("{} valor(es) impar(es)".format(imp))
print("{} valor(es) positivo(s)".format(pos))
print("{} valor(es) negativo(s)".format(neg))