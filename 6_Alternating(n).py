def Alternating(n) :
    count1 = 1
    count2 = -1
    sump = 0
    summ = 0
    while count1 < n :
        sump += count1
        count1 += 2
    while (count2)*(-1) < n :
        summ += count2
        count2 -= 2
        print(summ)
    sumn = sump + summ
    return sumn
n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n,Alternating(n)))