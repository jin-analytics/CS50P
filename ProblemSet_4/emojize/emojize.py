import sys
import requests
import json



r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r)

#response = requests.get("https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias")
#
#response.status_code

#data = response.content
#print(data)


