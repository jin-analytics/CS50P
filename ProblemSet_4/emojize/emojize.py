import sys
import requests




r = requests.get('https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias', auth=('user', 'pass'))

print(r.encoding())
#https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias


