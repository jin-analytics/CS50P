import sys
import requests
import json


#if len(sys.argv) != 2:
#    sys.exit()

response = requests.get("https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias")
#response = requests.response("https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias")
#response.json()
#for result in response:
    #print(json.dumps(r.json(), indent=2))
    #print(result["WRESTLERS"])
#res_json = response.json()
print(response.content)

#print(response.text)
