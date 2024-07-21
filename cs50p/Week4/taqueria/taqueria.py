MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    cost = 0
    while True:
        try:
            food = input("Item: ").title()
            for item in MENU:
                if food == item:
                    cost += MENU[item]
                    print(f"Total: ${cost:.2f}")
        except EOFError:
            return


main()
