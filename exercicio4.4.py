
num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite um número: "))

if num_1 < num_2:
    for n in range((num_1 + 1), num_2):
        print(n)

elif num_2 < num_1:
    for n in range((num_1 - 1), num_2, -1):
        print(n)

else:
    print("Os números são iguais")