n = str(input())
i = 0
if n.find(",") == -1 :
    if n.find(".") == -1 :
        print(int(n) + 1)
    elif n.find(".") != -1 :
        if len(n[n.rfind(".") + 1 : len(n) + 1 ]) > 2 :
            print("ERROR")
        else :
            print(float(n) + 1)
elif n.find(",") != -1 :
    while i < len(n) :
        if n[i] in "," :
            print(n[i + 1 : n.index(",")])
            if len(n[i + 1 : n.index(",")]) != 3 :
                print("ERROR")
                break
        elif i == len(n) -1 :
            print( n[0 : len(n) - 1] + str(int(n[len(n) - 1 : len(n) ]) + 1))
            break
        i += 1
else :
    print("ERROR")