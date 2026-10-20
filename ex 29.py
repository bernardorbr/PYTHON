media = float(input("Digite a média: "))
faltas = int(input("Digite a quantidade de faltas: "))

if media >= 7 and faltas <= 10:
    print("Aprovado")
elif media >= 5 and faltas <= 10:
    print("Recuperação")
else:
    print("Reprovado")