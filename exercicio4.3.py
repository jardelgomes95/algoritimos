
num = int(input("Insira um número: "))

while num < 0 or num > 10:
    print("Número inválido!")
    num = int(input("Insira um número: "))

    
for n in range(1, 11):
    print(num * n)