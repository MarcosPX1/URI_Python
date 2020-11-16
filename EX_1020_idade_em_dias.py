idade = int(input())

ano = idade // 365
idade = idade - ano * 365
meses = idade // 30
idade = idade - meses * 30

dias = idade

print(ano,"ano(s)")
print(meses,"mes(es)")
print(dias,"dia(s)")
