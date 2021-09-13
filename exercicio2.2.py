####!-*- coding: utf-8 -*-

#exercicios 2.2

num_horas = float(input("Informe o Número de horas trabalhadas: "))
valor_hora = float(input("Informe o valor da hora trabalhada: "))

salario_bruto = (num_horas * valor_hora)
inss = salario_bruto * 0.08
ir = salario_bruto * 0.11
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - inss - ir - sindicato

print("Salario Bruto:", salario_bruto, "INSS:", inss, "IR:", ir, "Sindicato:", sindicato, "Salario Liquido:", salario_liquido)