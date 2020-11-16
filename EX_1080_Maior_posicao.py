maior = 0
lista = {}
posicao = 0
while posicao < 5:  # Lerá 100 valores
    valor = int(input())
    if valor > maior:
        maior = valor  # Variavel maior recebe o valor indicado
        lista[valor] = posicao  # Lista recebe o valor e aloca para a variavel posicao
    posicao += 1
print(maior)
print(lista[maior] + 1)
