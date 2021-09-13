#Coding UTF -8


num_1 = float(input("Insira um número: "))
num_2 = float(input("Insira mais um número: "))
num_3 = float(input("Insira um ultimo número: "))

if num_1 < (num_2 and num_3):
    num_menor = num_1
elif num_2 < (num_1 and num_3):
    num_menor = num_2
else:
    num_menor = num_3

if num_1 > (num_2 and num_3):
    num_maior = num_1
elif num_2 > (num_1 and num_3):
    num_maior = num_2
else: 
    num_maior = num_3

print("O maior número é: ", num_maior, "E o menor número é: ", num_menor)