valor = float(input("Digite o valor: "))

if valor <= 1500:
    aumento = 0.20
elif valor <= 3000:
    aumento = 0.15
else:
    aumento = 0.10

novo_valor = valor + valor * aumento

print("Valor com aumento:", novo_valor)
