# importuri
import json
import requests
from pprint import pprint

url = "https://api.chucknorris.io/jokes/random"
# construi requestul cu metoda GET
raspuns = requests.get(url=url, params={})
# folosec modulul JSON pentru a transforma bytes in dict
gluma =  json.loads(raspuns.content)

pprint(gluma)
