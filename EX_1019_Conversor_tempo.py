valor = int(input())

horas = valor // 60 ** 2  # // - > Parte inteira
valor = valor - horas * 60 ** 2
minutos = valor // 60
valor = valor - minutos * 60
segundos = valor
print('{}:{}:{}'.format(horas,minutos,segundos))
