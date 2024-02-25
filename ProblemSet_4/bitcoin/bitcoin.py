import sys
import requests

try:
    coin = sys.argv[1]
except requests.RequestException:
    ...
