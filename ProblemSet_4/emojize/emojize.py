import sys
import requests
import json


if len(sys.argv) != 2:
    sys.exit()

#r = requests.get('https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias', auth=('user', 'pass'))
r= requests.get("https://itunes.apple.com/search?entity=song&limit1&term=" + sys.argv[1])


o = r.json()
for result in o["results"]:
    #print(json.dumps(r.json(), indent=2))
    print(result["trackName"])

#https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias


