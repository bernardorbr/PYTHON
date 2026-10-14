altura = float(input("Digite a altura em metros: "))
peso = float(input("Digite o peso em kg: "))

imc = peso / (altura ** 2)

print("IMC:", imc)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")