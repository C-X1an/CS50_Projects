VOWELS = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def main():
    text = input("Input: ")
    for vowel in VOWELS:
        text = text.replace(vowel, "")
    print("Output:" + text)

main()
