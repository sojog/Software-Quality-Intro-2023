# importuri
import json
import requests
from pprint import pprint

url = "https://api.chucknorris.io/jokes/search"
# construi requestul cu metoda GET
raspuns = requests.get(url=url, params={'query':'China'})
# folosec modulul JSON pentru a transforma bytes in dict
rezultat =  json.loads(raspuns.content)

pprint(type(rezultat))
# pprint(rezultat['result'])


# Varianta 1 - iteratie clasica
glume_politice = []
for i in rezultat['result']:
    if 'political' in i['categories']:
        glume_politice.append(i['value'])
print(glume_politice)

# Varianta 2 - List comprehension
glume_politice = [ i['value'] for i in rezultat['result'] if 'political' in i['categories']]
print(glume_politice)