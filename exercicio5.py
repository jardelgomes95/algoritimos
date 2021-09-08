####!-*- coding: utf-8 -*-

#questão 4.


sexo = bool(input("Você é Homem? "))
altura = int(input("Insira a altura em centimetros: "))

if sexo == True:
    print("O seu peso ideal é de", (altura * 0.727) - 58, "quilos")
else:
    print("O seu peso ideal é de", (altura * 0.621) - 44.7, "quilos")
