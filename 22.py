import math

numeros = []

for i in range(4):
    numeros.append(int(input("Digite um número: ")))

encontrou = False

for n in numeros:
    if n >= 0 and math.isqrt(n) ** 2 == n:
        encontrou = True

if encontrou:
    print("Existe um quadrado perfeito")
else:
    print("Não existe quadrado perfeito")