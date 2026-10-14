n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

notas = [n1, n2, n3, n4]

maior = max(notas)
menor = min(notas)

notas.remove(maior)
notas.remove(menor)

media = sum(notas) / 2

print("Média:", media)

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
