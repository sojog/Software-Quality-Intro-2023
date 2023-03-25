import requests
import json
from pprint import pprint

url = 'https://httpbin.org/post'
headers = {
    'Accept': 'application/json'
}
r = requests.post(url, headers=headers)
print(r.content)
print(type(r.content))