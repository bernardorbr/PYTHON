h1 = int(input("Hora 1: "))
m1 = int(input("Minuto 1: "))

h2 = int(input("Hora 2: "))
m2 = int(input("Minuto 2: "))

if h1 < h2 or (h1 == h2 and m1 < m2):
    print("O primeiro horário acontece primeiro")
elif h2 < h1 or (h2 == h1 and m2 < m1):
    print("O segundo horário acontece primeiro")
else:
    print("Os horários são iguais")