from cs50 import get_float


def main():

    while True:
        change = get_float("Change owed: ")
        if change > 0:
            break
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    while change > 0.24:
        change -= 0.25
        quarters += 1
    while change > 0.09:
        change -= 0.10
        dimes += 1
    while change > 0.04:
        change -= 0.05
        nickels += 1
    while round(change, 2) > 0:
        change -= 0.01
        pennies += 1

    coins = quarters + dimes + nickels + pennies
    print(coins)


main()
