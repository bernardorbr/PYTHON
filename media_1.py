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