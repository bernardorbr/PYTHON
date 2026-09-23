import getpass

senha = getpass.getpass("crie uma senha: ")
print("Senha criada com sucesso")

for tentativa in range(3):
    senha_digitada = getpass.getpass("Informe sua senha: ")
    
    if senha_digitada == senha: 
        print ("Acesso permitido")
        break
    else: 
        print("Acesso Negado")
else: 
    print("Acesso Bloqueado")
