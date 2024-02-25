import sys
import requests

try:
    if len(sys.argv) <2: #catches if there is less then one entree
        sys.exit("too few")
    if len(sys.argv) >2: #catches if there is more then one entree
        sys.exit("too many")

    coin = float(sys.argv[1]) #defines the n-amounts of coins
    print(coin)
    data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print(data.json())
    price = data.json()
except requests.RequestException:
    ...
