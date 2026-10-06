nome = str(input("Qual seu nome? \n"))
salario_bruto = float(input("Qual seu salario bruto? \n"))
percentual_desc_iss = float(input("Qual seu percentual de desconto do INSS? \n"))
percentual_desc_saude = float(input("Qual seu percentual de desconto do plano de saúde? \n"))

valor_inss = salario_bruto * (percentual_desc_iss/100)
valor_saude = salario_bruto * (percentual_desc_saude/100)
total_desconto = valor_inss + valor_saude
salario_liquido = salario_bruto - total_desconto 

print("=======================")
print("       Resultados      ")
print("=======================")
print(f"O valor do INSS é: {valor_inss}")
print(f"O valor do plano de saúde é: {valor_saude}")
print(f"o total de desconto é: {total_desconto}")
print(f"O salário líquido é: {salario_liquido}")
print("==================================")