import sys
import requests
import json


#if len(sys.argv) != 2:
#    sys.exit()

#r = requests.get('https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias', auth=('user', 'pass'))
response = requests.get("https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias")
#r = requests.post('https://httpbin.org/post', data={'key': 'value'})

#object = response.json()
#for result in object["results"]:
    #print(json.dumps(r.json(), indent=2))
r.tec
print(response)

#https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias


