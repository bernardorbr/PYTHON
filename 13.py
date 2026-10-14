n = int(input("Digite um número: "))

if n % 3 == 0 and n % 5 == 0:
    print("Divisível por 3 e por 5")
elif n % 3 == 0:
    print("Divisível apenas por 3")
elif n % 5 == 0:
    print("Divisível apenas por 5")
else:
    print("Não é divisível por 3 nem por 5")