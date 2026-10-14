n = float(input("Digite um número real: "))

parte_inteira = int(n)
parte_decimal = n - parte_inteira

if parte_decimal > 0.5:
    print("A parte decimal é maior que a parte inteira")
else:
    print("A parte decimal não é maior que a parte inteira")
