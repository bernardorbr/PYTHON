h1 = int(input("Hora 1: "))
m1 = int(input("Minuto 1: "))
s1 = int(input("Segundo 1: "))

h2 = int(input("Hora 2: "))
m2 = int(input("Minuto 2: "))
s2 = int(input("Segundo 2: "))

tempo1 = h1 * 3600 + m1 * 60 + s1
tempo2 = h2 * 3600 + m2 * 60 + s2

if tempo1 > tempo2:
    print("O primeiro horário é maior")
elif tempo2 > tempo1:
    print("O segundo horário é maior")
else:
    print("Os horários são iguais")