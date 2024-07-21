def main():
    fraction = input("Fraction: ")
    while True:
        try:
            nominator = int(fraction.split("/")[0])
            denominator = int(fraction.split("/")[1])
            fuel = round((nominator / denominator) * 100)
            if fuel > 100:
                raise ValueError
            break
        except ValueError:
            fraction = input("Fraction: ")
        except ZeroDivisionError:
            fraction = input("Fraction: ")
    if fuel >= 99:
        print("F")
    elif fuel <= 1:
        print("E")
    else:
        print(str(fuel) + "%")


main()
