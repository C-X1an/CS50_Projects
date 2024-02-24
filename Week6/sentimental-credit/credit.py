from cs50 import get_string


def main():
    number = get_string("Number: ")

    if len(number) not in [13, 15, 16]:
        print("INVALID")
        return 1

    set1 = number[-2::-2]
    sum_set1 = 0
    for chara in set1:
        chara = int(chara) * 2
        if chara > 9:
            chara = 1 + (chara % 10)
        sum_set1 += chara
    sum_set2 = 0
    set2 = number[-1::-2]
    for char in set2:
        sum_set2 += int(char)
    sum = int(sum_set1 + sum_set2)
    print(sum)
    if check(sum) == True:
        if len(number) == 15 and int(number[:2]) in [34, 37]:
            print("AMEX")
            return 0
        elif len(number) == 16 and int(number[:2]) in list(range(51, 56)):
            print("MASTERCARD")
            return 0
        elif len(number) == 13 or 16 and number[0] == '4':
            print("VISA")
            return 0
        else:
            print("INVALID")
            return 1
    else:
        print("INVALID")
        return 1


def check(sum):
    if sum % 10 == 0:
        return True
    else:
        return False


main()
