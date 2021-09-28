#Exercicios 3.3

numero = int(input("Digite um Número inteiro: "))

tot = 0

for x in range(1, numero + 1):
    if numero % x == 0:
        #print(x)
        tot += 1 
print("O número", numero,  "possuí", tot, "divisores!")

if tot <= 2:
    print("Logo: O numero", numero, "é primo!")
else: 
    print("Logo: O numero", numero, "não é primo!")