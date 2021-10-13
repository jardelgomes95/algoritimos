

popA = 80000
popB = 200000 

anos =  0


while popA < popB:
    anos += 1
    popA = popA + (popA * 0.03)
    popB = popB + (popB * 0.015)

print("Após", anos, "anos o país A ultrapassou o país B em número de habitantes." )

print(popA)
print(popB)

