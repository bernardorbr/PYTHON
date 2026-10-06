nome = input("Nome do motorista: \n")
distancia = float(input("Qual a distancia pecorrida em km? \n"))
litros = float(input("Quantos litros consumidos? \n"))
preco = float(input("Qual preço do litro do combustível? \n"))

consumo = distancia/litros 
gasto = litros*preco 

print("-------RESULTADO--------")
print("Motorista", nome)
print("Consumo médio", distancia, "Km/l")
print("Valor gasto",preco)