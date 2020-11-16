while True:
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
    teste = 0
    while True:
        print('novo calculo (1-sim 2-nao)')
        teste = int(input())
        if teste == 1 or teste ==2:
            break

    if teste == 2:
        break
