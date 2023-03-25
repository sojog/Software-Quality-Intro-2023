import requests
from pprint import pprint
import json

# Url-ul site-ului
base_url = 'https://api.datamuse.com/'

# Path compus
path = 'words'

url = base_url + path

# Creez cererea HTTP de tip GET cu parametri
response = requests.get(url, params={ "ml":"sunny" ,"rel_rhy":"day"})

# Verific url-ul format
print(response.request.url)

# Raspunsul este transformata in lista din JSON
words = json.loads(response.content)
pprint(words)

print(type(words))

cuvinte = [  i['word']    for i in words  ]
print(cuvinte)