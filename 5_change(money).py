def change(money,change_to) :
    changed = money // change_to
    return changed
money = int(input("Enter total money: "))
b500 = change(money,500)
print(b500,"b500")
left = money - b500*500
b100 = change(left,100)
print(b100, "b100")
left = left - b100*100
b20 = change(left,20)
left = left - b20*20
print(b20 , "b20")
b5 = change(left,5)
left = left - b5*5
print(b5 , "b5")
b1 = change(left,1)
print(b1 , "b1")


print("500: %d" % b500)
print("100: %d" % b100)
print(" 20: %d" % b20)
print("  5: %d" % b5)
print("  1: %d" % b1)