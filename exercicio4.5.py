
n1 = float(input("Insira a nota N1: "))
n2 = float(input("Insira a nota N2: "))

while n1 < 0 or n1 > 10:
    print("Nota inválida!")
    n1 = float(input("Insira a nota N1: "))
    
while n2 < 0 or n2 > 10:
    print("Nota inválida!")
    n2 = float(input("Insira a nota N2: "))


media = (n1 + n2)/2

if media >= 9:
    print('A média foi', media, "Conceito A")
elif media >= 7.5 or media < 9:
    print('A média foi', media, "Conceito B")
elif media >= 6 or media < 7.5:
    print('A média foi', media, "Conceito C")
elif media >= 4 or media < 6:
    print('A média foi', media, "Conceito D")
else:
    print('A média foi', media, "Conceito E")