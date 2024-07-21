MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        check = 0
        date = input("Date: ")
        if date[0].isalpha():
            try:
                month, day, year = date.split(" ")
                if day.find(",") == -1:
                    check = 1
                day = day.replace(",", "")
                if month in MONTHS:
                    month = MONTHS.index(month) + 1
                else:
                    check = 1
            except ValueError:
                check = 1
        else:
            try:
                month, day, year = date.split("/")
                if int(month) > 12:
                    check = 1
            except ValueError:
                check = 1
        try:
            if int(day) > 31:
                check = 1
        except UnboundLocalError:
            check = 1
        if check != 1:
            break
    print(year.strip(), end="-", sep="")
    if int(month) < 10:
        print("0" + str(month).strip(), end="-", sep="")
    else:
        print(month, end="-", sep="")
    if int(day) < 10:
        print("0" + day)
    else:
        print(day)

main()
