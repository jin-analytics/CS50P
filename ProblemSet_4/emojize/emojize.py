import sys
import requests




#r = requests.get('https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias', auth=('user', 'pass'))
r= requests.get("https://itunes.apple.com/search?entity=song&limit01&term=" + sys.argv[1])
print(r.json())
#https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias


