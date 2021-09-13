#Coding utf -8


n1 = float(input("Insira a nota 1: "))
n2 = float(input("Insira a nota 2: "))

media = (n1 + n2) / 2

if media < 7:
    print("A média do aluno foi", media, "Portanto, o aluno está REPROVADO")

elif media == 10:
    print("A média do aluno foi", media, "Portanto, o aluno foi APROVADO com distinção")
    
else:
    print("A média do aluno foi", media, "Portanto, o aluno está APROVADO")
