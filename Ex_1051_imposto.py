Salario = float(input())
impos8 = 0.08
impos18 = 0.18
impost28 = 0.28

if Salario > 0 and Salario <= 2000:
    print("Isento")
elif Salario > 2000 and Salario <= 3000:
    resto = Salario - 2000
    calc = resto * impos8
    print("R$ {:.2f}".format(calc))
elif Salario > 3000 and Salario < 4500:
    resto = Salario - 3000
    calc = (resto * impos18) + (1000 * impos8)
    print("R$ {:.2f}".format(calc))
else:
    resto = Salario - 4500
    calc = (resto * impost28) + (1500 * impos18) + (1000 * impos8)
    print("R$ {:.2f}".format(calc))
