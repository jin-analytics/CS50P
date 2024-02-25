import sys
import requests
import json

try:
    if len(sys.argv) <2: #catches if there is less then one entree
        sys.exit("too few")
    if len(sys.argv) >2: #catches if there is more then one entree
        sys.exit("too many")

    coins = float(sys.argv[1]) #defines the n-amounts of coins
    #print(coins)
    data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin = data.json()
    print(json.dumps(bitcoin, indent = 2))
    for result in bitcoin["bpi"]:
        print(result.get("USD"))
except requests.RequestException:
    ...
