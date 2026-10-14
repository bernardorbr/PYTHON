n = int(input("Digite um número de 5 dígitos: "))

if 10000 <= n <= 99999:
    if str(n) == str(n)[::-1]:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")
else:
    print("Número inválido")