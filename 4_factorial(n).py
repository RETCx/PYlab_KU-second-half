def Alternating(n) :
    minussumn = 0 
    plussumn = 0
    al = 1
    count = 0 
    while count <= n :
        if al % 2 == 0 :
            minussumn += (al)     
            al += 1
            count += 1  
            continue
        else :
            plussumn -= al
            al += 1
            count += 1  
            continue
    sumn = minussumn + plussumn

    return sumn
n = int(input("Enter n of series: "))
print(Alternating(n))

        