import sys
import requests
import json

try:
    if len(sys.argv) <2: #catches if there is less then one entree
        sys.exit("too few")
    if len(sys.argv) >2: #catches if there is more then one entree
        sys.exit("too many")

    coins = float(sys.argv[1]) #defines the n-amounts of coins
    data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin = data.json()
    #print(json.dumps(bitcoin, indent = 2)) #shows the data of the request in nice readable form
    price = bitcoin["bpi"]["USD"]["rate_float"].replace
    print(price)


except requests.RequestException:
    ...
