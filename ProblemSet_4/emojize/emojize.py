import sys
import requests
import json

response = requests.get("https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias")

response.status_code

data = response.content
print(data)


