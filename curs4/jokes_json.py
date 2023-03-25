import requests
import json
from pprint import pprint

url = 'https://icanhazdadjoke.com/'
headers = {
    'Accept': 'application/json'
}
r = requests.get(url, headers=headers)
pprint(r.content)
print(type(r.content))

r_dict = json.loads(r.content)
print(r_dict)
