import sys
import requests

try:
    coin = sys.argv[1]
    print(coin)
    data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print(data.json())
except requests.RequestException:
    ...
