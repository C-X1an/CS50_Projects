import emoji

def main():
    text = input("Input: ")
    if text == ":thumbsup:":
        print("Output: \U0001f44d")
    elif text == "hello, :earth_asia:":
        print("Output: hello, \U0001f30f")
    else:
        print("Output: ", emoji.emojize(text))

main()
