

saque = int(input('Digite o valor do saque: '))

total = saque

ced = 100

totced = 0 

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(totced, "de", ced)
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1 
        
        totced = 0 
        if total == 0:
            break
        


