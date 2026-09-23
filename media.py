a = input("Digite o nome do aluno: \n"  )

b = float(input("Informe a Primeira Nota: \n"))
c = float(input("Informe a Segunda Nota: \n"))
d = float(input("Informe a Terceira Nota: \n"))

media = (float (b + c + d))/3

if media >= 6:
    print("Parabéns" ,a, "Aprovado")
elif media <=5: 
    print("Aluno de Recuperação")
else: 
    print("Aluno Reprovado")
    
    