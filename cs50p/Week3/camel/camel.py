def main():
    camel = input("camelCase: ")

    print("snake_case: ")

    for character in camel:
        if character.isupper():
            character = character.lower()
            character = character.replace(character, "_" + character)
            character = character.replace(" ", "")
        print(character, end="")
    print()

main()
