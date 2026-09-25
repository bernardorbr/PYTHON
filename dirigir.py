a = str(input("Informe se Nome: \n"))
b = str(input("Você bebeu? \n"))
c = str(input("Você tem carteira de motorista? \n"))

if b == "não" and c == "sim":
    print("Senhor" , a , "você pode dirigir")
else:
    print("Senhor" , a ,"você não pode dirigir")