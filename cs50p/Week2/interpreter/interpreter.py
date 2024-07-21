def main():
    express = input("Expression: ")
    x, y, z = express.split(" ")
    if y == "+":
        answer = int(x) + int(z)
    elif y == "-":
        answer = int(x) - int(z)
    elif y == "*":
        answer = int(x) * int(z)
    elif y == "/":
        answer = int(x) / int(z)

    print(round(float(answer), 1))

main()
