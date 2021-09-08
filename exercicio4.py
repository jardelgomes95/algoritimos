####!-*- coding: utf-8 -*-

#questão 4.

peso = int(input("insira o peso: "))

if peso <= 50:
    print("Não há multa a pagar!")
elif peso > 50:
    print("A multa a pagar é de", (peso - 50) * 4, "Reais")