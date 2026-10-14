a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))
d = int(input("Número 4: "))

numeros = [a, b, c, d]

if len(set(numeros)) < 4:
    print("Existe um quadrado perfeito entre eles")
else:
    print("Não existe quadrado perfeito entre eles")