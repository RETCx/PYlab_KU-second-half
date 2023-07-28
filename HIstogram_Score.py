n = str(input())
i = 0
a = ""
check = True
while i < len(n) :
    if n[i] in "abcdefghijklmonpqrstuvwxyz" :
            a = "ERROR"
            break  
    i += 1
if a == "ERROR" :
    print(a)
else :
    if n.find(",") == -1 :
        if n.find(".") == -1 :
            print(int(n) + 1)
        elif n.find(".") != -1 :
            if (len(n[n.rfind(".") + 1 : len(n) + 1 ]) > 2 ) or (len(n[n.rfind(".") + 1 : len(n) + 1 ]) <= 0)  :
                print("ERROR")
            elif n.count(".") > 1 :
                print("ERROR")
            else :
                print(f"{float(n) + 1:.2f}")
    elif n.find(",") != -1 :
        i = 0
        while i < len(n) :
            if n[i] in "," :
                if len(n[i + 1 : len(n)]) != 3 :
                    print("ERROR")
                    check = False
                    break
            elif i == len(n) -1 :
                if n.find(",") == 0 :
                    print("ERROR")
                    check = False
                    break
                else :
                    pass
            i += 1
        if n[n.rfind(",")] == n[-1] and check :

            print("ERROR")
        elif check :
            x = n.replace(",", "")
            if n[-3] in "." :
                if n[n.rfind(".") - 4 ] not in "," :

                    print("ERROR")
                else :
                    print( str(int(x[0 : x.find(".")]) + 1 ) + x[x.find("."): len(x)])
            elif (len(n[n.rfind(".") + 1 : len(n)] )> 2 ) and ( n.count(".") > 0 ):
                print("ERROR") 
            else :
                print(int(x) + 1)
        


        

