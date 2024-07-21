import requests
import sys

def main():
    try:
        amount = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    cost = get_price(amount)
    print(f"${cost:,}")

def get_price(amount):
    try:
        jsoninfo = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        price = float(jsoninfo["bpi"]["USD"]["rate_float"])
        return price * amount
    except requests.RequestException:
        ...

main()
