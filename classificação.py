<<<<<<< HEAD
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
=======
name = input('Digite seu nome: ')
a = int(input('Digite a primeria nota: '))
b = int(input('Digite a segunda nota: '))
c = int(input('Digite a terceira nota: '))
media= (a+b+c)/3
if media <6:
  print('Reprovado',name,  media) 
elif media <6 and media >4:
  print('Recuperação')
else:
  print ('Aprovado',name,  media)
>>>>>>> aff3f95 (Sistema de senha)
