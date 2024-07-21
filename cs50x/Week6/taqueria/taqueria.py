def main():
    menu = {
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
    total = 0
    while True:
        try:
            item = input("Item: ")
        except EOFError:
            print()
            return 0
        item = item.capitalize()
        if ' ' in item:
            for i in range(len(item)):
                if item[i] == ' ':
                    new_item = item[:i + 1] + item[i + 1].upper() + item[i + 1 + 1:]
                    if new_item in menu:
                        total += float(menu[new_item])
                        print(f"${total:.2f}")
        if item in menu:
            total += float(menu[item])
            print(f"${total:.2f}")
        if item == "":
            return 0

main()
