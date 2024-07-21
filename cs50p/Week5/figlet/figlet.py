from pyfiglet import Figlet, FigletFont
import sys

ACCEPTED_FONTS = FigletFont.getFonts()

def main():
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit("Invalid Usage")
    elif sys.argv[1] != "-f":
        sys.exit("Invalid Usage")
    elif sys.argv[2] not in ACCEPTED_FONTS:
        sys.exit("Invalid Usage")
    text = input("Input: ")
    if len(sys.argv) == 3:
        print(Figlet(font=sys.argv[2]).renderText(text))
    else:
        print(Figlet().renderText(text))

main()
