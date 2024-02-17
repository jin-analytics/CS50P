import sys
import requests
import json

.get("https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias")

data = response.json()
thumbs = data["detective"]
print(data)


