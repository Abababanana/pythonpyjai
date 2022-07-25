"""เบื่อแล้วขนมตู้_อยากเป็นชู้กับเธอ"""
def main():
    money = int(input())
    water = int(input())
    snack1 = int(input())
    snack2 = int(input())
    snack3 = int(input())
    money_use = (money-water)%3
    if money_use == 0:
        expense1 = money-(water+(10*snack1))
    elif money_use == 1:
        expense1 = money-(water+(15*snack1))
    elif money_use == 2:
        expense1 = money-(water+(20*snack1))
    money_use2 = expense1%3
    if money_use2 == 0:
        expense2 = expense1-(12*snack2)
    elif money_use2 == 1:
        expense2 = expense1-(15*snack2)
    elif money_use2 == 2:
        expense2 = expense1-(18*snack2)
    money_use3 = expense2%3
    if money_use3 == 0:
        expense3 = expense2-(5*snack3)
    elif money_use3 == 1:
        expense3 = expense2-(7*snack3)
    elif money_use3 == 2:
        expense3 = expense2-(9*snack3)
    if expense3 < 0:
        print("Now you have %d" %money +" left.")
        print("You don't have enough money!")
    else:
        print("Now you have %d" %expense3 +" left.")
        print("Here's your order!")
        print("Water: %d" %water +" baht")
        print("Snack number 1: %d" %snack1 +" baht")
        print("Snack number 2: %d" %snack2 +" baht")
        print("Snack number 3: %d" %snack3 +" baht")
main()
    

    
