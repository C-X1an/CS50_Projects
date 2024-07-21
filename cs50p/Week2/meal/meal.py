def main():
    time = input("What time is it? ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    try:
        if time.find("p.m.") >= 0:
            time = time.split(" ")[0]
            if int(time.split(":")[0]) == 12:
                time = int(time.split(":")[0]) + (int(time.split(":")[1]) / 60)
            else:
                time = int(time.split(":")[0]) + 12 + (int(time.split(":")[1]) / 60)
        elif time.find("a.m.") >= 0:
            time = time.split(" ")[0]
            if int(time.split(":")[0]) == 12:
                time = int(time.split(":")[0]) - 12 + (int(time.split(":")[1]) / 60)
            else:
                time = int(time.split(":")[0]) + 12 + (int(time.split(":")[1]) / 60)
        else:
            time = int(time.split(":")[0]) + (int(time.split(":")[1]) / 60)
    except IndexError:
        print("Invalid time")
        return

    return time

if __name__ == "__main__":
    main()
