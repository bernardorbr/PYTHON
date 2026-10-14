dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

if 1 <= mes <= 12 and 1 <= dia <= 31:
    print("Data aparentemente válida")
else:
    print("Data inválida")
