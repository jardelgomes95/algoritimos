#Exercicios 3.2  SOMA DE NÚMEROS ÍMPARES
soma = 0


for x in range(0, 100):
    if x % 2 != 0:
        soma += x      #SOMA RECEBE SOMA + 1      /// #operador aritimético de atribuição, quando tenho um valor fixo pre determinado (soma = 0) mais uma váriável (contador X). 
print(soma)
