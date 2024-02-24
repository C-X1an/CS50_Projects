from cs50 import get_string


def main():
    text = get_string("Text: ")

    letters = 0
    words = 0
    sentence = 0
    for character in text:
        if character.isalpha():
            letters += 1
        elif character in ['.', '!', '?']:
            sentence += 1
        elif character == ' ':
            words += 1
    words += 1
    L = (letters / words) * 100
    S = (sentence / words) * 100

    index = round(0.0588 * L - 0.296 * S - 15.8)
    if index > 16:
        print("Grade 16+")
        return 0
    elif index < 1:
        print("Before Grade 1")
    else:
        print("Grade", index)


main()
