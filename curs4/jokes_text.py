import requests
import json
from pprint import pprint

url = 'https://icanhazdadjoke.com/'
headers = {
    'Accept': 'text/plain'
}
r = requests.get(url, headers=headers)
pprint(r.content)

with open('glume_bune_2023.txt', 'ab') as f:
    f.write(r.content)
    f.write(bytes("\n\n", encoding="utf-8"))


