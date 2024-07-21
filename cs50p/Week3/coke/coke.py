COST = 50
VALID_PAY = [5, 10, 25]

def main():
    due = COST
    while due > 0:
        print("Amount Due: " + str(due))
        pay = int(input("Insert Coin: "))
        while True:
            if pay in VALID_PAY:
                break
            else:
                print("Amount Due: " + str(due))
                pay = int(input("Insert Coin: "))
        due -= pay
    print("Change Owed: " + str(-1 * due))

main()
