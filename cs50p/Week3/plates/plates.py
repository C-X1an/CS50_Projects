def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if s[0].isalpha() == False:
        return False
    if s[1].isalpha() == False:
        return False
    for char in s:
        if char.isnumeric():
            if char == "0":
                return False
            else:
                break
    for count, char in enumerate(s):
        if char.isnumeric():
            while count < len(s) - 1:
                if s[count].isalpha():
                    return False
                else:
                    count += 1
    for char in s:
        if char.isalnum() == False:
            return False
    return True

main()
