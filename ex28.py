caractere = input("Digite um caractere: ")

if caractere.isupper():
    print("Letra maiúscula")
elif caractere.islower():
    print("Letra minúscula")
elif caractere.isdigit():
    print("Número")
else:
    print("Símbolo")
