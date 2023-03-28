""" HTTP Requests to predict the nationality of a name
"""

# importuri
import json
import requests
import pprint


# construiesc URL 
url = "https://api.nationalize.io/"

# definire nume 
nume = "Silviu"

# Parametri formea urmatorul link https://api.nationalize.io/?name=silviu
parametri  = { "name" : nume}

# construi requestul cu metoda GET
raspuns = requests.get(url=url, params=parametri)
# print(raspuns)
# print(raspuns.status_code)
# print(raspuns.content)
# print(type(raspuns.content))


# folosec modulul JSON pentru a transforma bytes in dict
probabilitati =  json.loads(raspuns.content)
# print(probabilitati)
# print(type(probabilitati))

# pprint.pprint(probabilitati)
pprint.pprint(probabilitati['country'])
# pprint.pprint(probabilitati['country'][0])
pprint.pprint(probabilitati['country'][0]['probability'])



# Version 1 - 
tari = []
for i in probabilitati['country']:
    # print(i)
    # print(i['country_id'])
    tari.append(i['country_id'])

# Version 2 - list comprehension
tari = [ (i['country_id'], i['probability'])  for i in probabilitati['country']]
print(f'Numele {nume} provine din urmatoarele tari {tari}')

tari = [ i['country_id']  + ' cu probabilitatea ' +  "{:.2f}".format(i['probability']*100) + '%'  for i in probabilitati['country']]
tari = ", ".join(tari)
print(tari)

print(f'Numele {nume} provine din urmatoarele tari {tari}')