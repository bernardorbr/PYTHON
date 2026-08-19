a= input('Me diga seu nome: \n')
b= float(input("Me informe sua média geral do 1ª Bimestre: "))
c= float(input("Me informe a sua média de geral do 2ª Bimestre: "))

media= (b+c)/2

if media >= 8:
    print("Você está na turma A")

elif media < 8 and media > 6:
    print("Você está na Turma B")
    
else:
    print("você está na turma C")