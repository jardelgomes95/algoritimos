
nota = float(input("Digite uma nota:"))

while nota < 0 or nota > 10:
    print("Nota Inválida!")

    nota = float(input("Digite uma nota:"))

print("A nota digitada foi", nota)