a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

lados = sorted([a, b, c])

if lados[0] ** 2 + lados[1] ** 2 == lados[2] ** 2:
    print("Podem formar um triângulo retângulo")
else:
    print("Não formam um triângulo retângulo")