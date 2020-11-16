cont = 0

for i in range(0,5):
    i = int(input())
    if (int(i) % 2) == 0:
        cont += 1
print("{} valores pares".format(cont))
