####!-*- coding: utf-8 -*-

#exercicios 2.3

area = float(input("Informe o tamanho da area a ser pintada em m²: "))

lata_tinta = 3 * 18


if area % lata_tinta != 0: #se o resto da divisão for diferente de zero
    n_latas = (area // lata_tinta) + 1   #divisão inteira = desconsidera o resto ///// evitará a falta de tinta
else:
    n_latas = area / lata_tinta

resto = area % lata_tinta 
sobra = (resto / lata_tinta) #informará quantos litros de tinta irá sobrar caso venha a sobrar

print("Para realizar a pintura é necessário comprar ", n_latas, "latas de tinta e sobrará ", sobra, "latas de tinta")