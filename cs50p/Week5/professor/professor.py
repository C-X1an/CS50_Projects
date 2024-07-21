import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        wrong = 0
        first_number = generate_integer(level)
        second_number = generate_integer(level)
        answer = first_number + second_number
        while True:
            print(first_number, "+", second_number, "= ", end="")
            attempt = int(input(""))
            if attempt != answer:
                print("EEE")
                wrong += 1
            if wrong == 3:
                print(first_number, "+", second_number, "=", answer)
                break
            if attempt == answer:
                score += 1
                break
    print("Score:", score)




def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
