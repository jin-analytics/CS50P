import sys
import requests
import json


#if len(sys.argv) != 2:
#    sys.exit()

response = requests.get("https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias")

#response.json()
print(response.text)
#print(response.text)
