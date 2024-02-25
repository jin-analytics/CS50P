import sys
import requests
import json

try:
    if len(sys.argv) <2: #catches if there is less then one entree
        sys.exit("Missing command-line argument")
    if len(sys.argv) >2: #catches if there is more then one entree
        sys.exit("too many")

    coins = float(sys.argv[1]) #defines the n-amounts of coins
    data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin = data.json()
    #print(json.dumps(bitcoin, indent = 2)) #shows the data of the request in nice readable form
    price = bitcoin["bpi"]["USD"]["rate_float"] * coins
    #print(f"${price:,}") #uses comma to thousand seperator (per default are 4 digits behind comma)
    print(f"${price:,.4f}") #uses comma to thousand seperator and cuts after 2 digits behind comma


except requests.RequestException:
    ...
