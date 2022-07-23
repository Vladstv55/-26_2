with open('Задание2.txt') as f:    
    n = int(f.readline())   
    ob_sr = 0   
    for s in f:
        bal = list(map(int, s.split()))    
        sr = (sum(bal)) / 3    
        ob_sr += sr     
    itog = ob_sr / 10000   
with open('Задание2.txt') as f:    
    n = int(f.readline())  
    otvet1 = 0     
    otvet2 = 0     
    for s in f:
        bal = list(map(int, s.split()))    
        bal.sort()     
        sr = (sum(bal)) / 3    
        if sr < itog:   
            otvet1 += 1
            if (bal[2] > 85) and (bal[1] <= 85) and (bal[2] - bal[0] > 35):     
                otvet2 += 1
print(otvet1, otvet2)