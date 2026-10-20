caractere = input("Digite um caractere: ")

if caractere.isalpha():
    print("Vogal" if caractere.lower() in "aeiou" else "Consoante")
elif caractere.isdigit():
    print("Número")
else:
    print("Símbolo")
