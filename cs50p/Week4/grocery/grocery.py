grocery = []

def main():
    while True:
        try:
            check = 0
            food = input("").upper()
            for dict in grocery:
                if dict['food'] == food:
                    dict['count'] += 1
                    check = 1
            if check == 0:
                grocery.append({'food': food, 'count': 1})
        except EOFError:
            break

    grocery.sort(key=myFunc)

    for item in grocery:
        print(str(item['count']) + " " + item['food'])

def myFunc(e):
  return e['food']

main()

