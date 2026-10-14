a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

if a + b > c and a + c > b and b + c > a:

    if a == b == c:
        print("Equilátero")

    elif a == b or a == c or b == c:
        print("Isósceles")

    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Retângulo")

    else:
        print("Escaleno")

else:
    print("Não podem formar um triângulo")