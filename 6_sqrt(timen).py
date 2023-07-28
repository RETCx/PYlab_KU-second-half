def sqrt_n_times(x, n) :
    sqrtcount = 0
    while sqrtcount < n :
        x = x**(1/2)
        sqrtcount += 1
    return x
x = float(input())
n = int(input())
print( sqrt_n_times(x, n) )