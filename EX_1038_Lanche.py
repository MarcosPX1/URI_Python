x = input().split(" ")
codigo, qtd = x
codigo = int(codigo)
qtd = int(qtd)

if codigo == 1:
    total = qtd * 4.00
    print("Total: R$ {:.2f}".format(total))
if codigo == 2:
    total = qtd * 4.50
    print("Total: R$ {:.2f}".format(total))
if codigo == 3:
    total = qtd * 5.00
    print("Total: R$ {:.2f}".format(total))
if codigo == 4:
    total = qtd * 2.00
    print("Total: R$ {:.2f}".format(total))
if codigo == 5:
    total = qtd * 1.50
    print("Total: R$ {:.2f}".format(total))

