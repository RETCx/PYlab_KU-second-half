def factor_count(n) :
    count = 0
    divide = 1 
    while True :
        n_divide = n % divide
        print(divide)
        if n_divide == 0 :
            count += 1
            divide += 1
        else :
            divide += 1
        if divide == n :
            count += 1
            break
    return count
n = int(input("Enter n: "))
c = factor_count(n)
print(c)
