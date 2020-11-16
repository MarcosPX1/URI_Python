qte = int(input())

# Loop para retornar a quantidade de valores indicado

for i in range(qte):
    valor = int(input())
# Verifica se o valor é par
    if (valor % 2 == 0):
        if (valor == 0):
            print("NULL")
        if (valor > 0):
            print("EVEN POSITIVE")
        else:
            if (valor < 0):
                print("EVEN NEGATIVE")
    else:
        if (valor > 0):
            print("ODD POSITIVE")
        else: # imprime o valor ímpar de qualquer número
            print("ODD NEGATIVE")
