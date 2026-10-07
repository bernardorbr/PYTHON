idade = int(input("Informe sua idade: \n"))

if idade <18:
    print("menor de idade")
elif idade >= 18 and idade <60:
    print("Adulto")
else:
    print("Idoso(a)")