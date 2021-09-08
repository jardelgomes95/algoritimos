####!-*- coding: utf-8 -*-

temp = float(input("entre com a temperatura"))

if temp < 0:
    print("congelando")
elif 0 <= temp <= 20:
    print("Frio")
elif 21 <= temp <= 25:
    print("Normal")
elif 26 <= temp <= 35:
    print("Quente")
else:
    print("Muito Quente")
