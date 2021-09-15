#Coding Utf -8


lado_A = float(input("Isira um valor A: "))
lado_B = float(input("Insira um valor B: "))
lado_C = float(input("Insira um valor C: "))

#É um triangulo? 

if ((lado_A + lado_B) > lado_C) and ((lado_B + lado_C) > lado_A) and ((lado_C + lado_A) > lado_B):
    if (lado_A == (lado_B and lado_C)):
        print("É um triângulo equilátero")
    elif lado_A == (lado_B or lado_C) or lado_B == (lado_A or lado_C) or lado_C == (lado_A or lado_B):
        print("É um triângulo Isósceles")
    else:
        print("É um triângulo Escaleno")
else:
    triangulo = False
    print("Não é um triângulo")

