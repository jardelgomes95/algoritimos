
soma = 0
mult = 1

for x in range(1, 6):
    num = float(input("Digite um número: "))
    soma += num
    mult *= num
    
media = soma / 5   

print("A soma dos números é:", soma)

print("A multiplicação dos números é:", mult)

print("A média dos números é:", media)