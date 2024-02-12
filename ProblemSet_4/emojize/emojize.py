import sys
import requests
import json


if len(sys.argv) != 2:
    sys.exit()

#r = requests.get('https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias', auth=('user', 'pass'))
r= requests.get("https://itunes.apple.com/search?entity=song&limit1&term=trackname=" + sys.argv[1])
print(json.dumps(r.json(), indent=2))



#https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias


