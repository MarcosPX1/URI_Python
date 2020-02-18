"""
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
"""
"""
A = float(input())
B = float(input())
C = float(input())
pi = float(3.14159)

Area_tri = (A * C)/2
Area_cir = pi * (C ** 2)
Area_trap = C * (A + B)/2
Area_quad = B ** 2
Area_ret = A * B

print("TRIANGULO: {:.3f}".format(Area_tri))
print("CIRCULO: {:.3f}".format(Area_cir))
print("TRAPEZIO: {:.3f}".format(Area_trap))
print("QUADRADO: {:.3f}".format(Area_quad))
print("RETANGULO: {:.3f}".format(Area_ret))
"""
# Formula correta com separação de Strings
valor = input().split(" ")

a, b, c = valor
pi = 3.14159

triangulo = (float(a) * float(c))/2
circulo = pi * (float(c)* float(c))
trapezio = float(c) *(float(a) + float(b)) / 2
quadrado = float(b) * float(b)
retangulo = float(a) * float(b)


print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (triangulo, circulo, trapezio, quadrado, retangulo))