
salario = float(input("Informe o salário: "))

mult = 0.0075


for n in range(1, 17):
    mult *= 2
    print((mult +1) * salario)


