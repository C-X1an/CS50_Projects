from random import randint
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            while level < 1:
                level = int(input("Level: "))
            break
        except ValueError:
            pass
    answer = randint(1, level)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > answer:
                print("Too large!")
            elif guess < answer:
                print("Too small!")
            else:
                print("Just right!")
                sys.exit("")
        except ValueError:
            pass

main()
