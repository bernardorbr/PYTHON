idade = int(input("Digite a idade: "))
contribuicao = int(input("Digite o tempo de contribuição: "))

if idade >= 65 or contribuicao >= 35:
    print("Pode se aposentar")
else:
    print("Não pode se aposentar")