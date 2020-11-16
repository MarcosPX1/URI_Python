soma = 0 # ira receber o valor da nota 2x
qte = 0
while qte < 2:
    nota = float(input())
    if(nota >= 0 and nota <= 10):
        soma += nota  # soma o valor da nota na V - Soma
        qte += 1  # incremento para o looping
    else:
        print("nota invalida")

print("media = %.2f" %(soma/2))