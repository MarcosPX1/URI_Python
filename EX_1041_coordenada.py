# -*- coding: utf-8 -*-
# URI EXERCISE 1041
linha = input().split(" ")

x, y = linha

x = float(x)
y = float(y)

if x == 0.0 and y == 0.0:
    print('Origem')
elif x >= 0.1 and y >= 0.1:
    print('Q1')
elif x < 0.0 and y >= 0.1:
    print('Q2')
elif x < 0.0 and y < 0.0:
    print('Q3')
elif x > 0.0 and y < 0.0:
    print('Q4')
elif (x > 0.0) or (x < 0.0) and y == 0.0:
    print('Eixo X')
elif (y > 0.0) or (y < 0.0) and x == 0.0:
    print('Eixo Y')
