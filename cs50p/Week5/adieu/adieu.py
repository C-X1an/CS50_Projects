def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break
    print()
    print("Adieu, adieu, to ", end="")
    for count, item in enumerate(names):
        if count == len(names) - 1 and len(names) > 2:
            print(", and", item)
        elif count == len(names) - 1 and len(names) > 1:
            print(" and", item)
        elif len(names) == 1:
            print(item)
        elif count > 0:
            print(",", item, end="")
        else:
            print(item, end="")
main()
