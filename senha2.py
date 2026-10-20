senha_correta = "81861016"

senha = input("Digite a sua senha: \n")

while senha != senha_correta:
    print("senha Incorreta! Tente novamente.")
    senha = input("Digite novamente: \n")
print("Acesso permitido")