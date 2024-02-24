from cs50 import get_int


def main():
    height = 9
    while height < 1 or height > 8:
        height = get_int("Height: ")

    for n in range(height):
        for i in range(height - n - 1):
            print(' ', end='')
        print('#' * (n + 1), end='')
        print()


main()
