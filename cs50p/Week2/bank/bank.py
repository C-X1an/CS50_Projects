def main():
    greeting = input("Greeting: ")
    greeting = greeting.strip().capitalize()

    if greeting.find("Hello") >= 0:
        print("$0")
    elif greeting.find("H") == 0:
        print("$20")
    else:
        print("$100")

main()
