v1 = float(input("Digite o valor 1: "))
v2 = float(input("Digite o valor 2: "))
v3 = float(input("Digite o valor 3: "))

if v1 > v2 and v1 > v3:
    maior = v1
elif v2 > v1 and v2 > v3:
    maior = v2
elif v3 > v1 and v3 > v2:
    maior = v3

if v1 < v2 and v1 < v3:
    menor = v1
elif v2 < v1 and v2 < v3:
    menor = v2
elif v3 < v1 and v3 < v2:
    menor = v3

print("Maior valor: %d " % maior)
print("Menor valor: %d " % menor)