import sys
from pyfiglet import Figlet

def main():
    print(f"{Figlet.getFonts()}")
    if len(sys.argv) != (3 or 1):
        print("Invalid usage")
        sys.exit(1)
    elif len(sys.argv) == 3:
        if sys.argv[1] != ("-f" or "--font"):
            print("Invalid usage")
            sys.exit(1)
        if sys.argv[2] in Figlet.getFonts():
            i = i + 0
        else:
            print("Invalid usage")
            sys.exit(1)

    text = input("Input: ")
    if argv[2] != "":
        Figlet.setFont(font=argv[2])
    print(Figlet.renderText(text))

main()
