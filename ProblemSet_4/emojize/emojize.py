import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
response = requests.get("https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias")

o = response.json()
for result in o:
