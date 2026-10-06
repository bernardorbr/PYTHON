a = str(input("Digite seu nome: \n"))
b = str(input("Você bebeu? \n"))
c = str(input("Você tem carteira de motorista? \n"))

if b == "sim" and c == "não":
    print("Senhor",a,"você pode dirigir!")
else:
    print("senhor",a,"você não pode dirigir!")