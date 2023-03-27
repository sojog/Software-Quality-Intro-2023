# importuri
import json
import requests
import pprint


# construiesc URL 
url = "https://api.nationalize.io/"

# definire nume 
nume = "Silviu"

# ?name=silviu
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

    # Version 1
    # tari = []
    # for i in probabilitati['country']:
    #     # print(i)
    #     # print(i['country_id'])
    #     tari.append(i['country_id'])

# Version 2



tari = [ (i['country_id'], i['probability'])  for i in probabilitati['country']]
print(f'Numele {nume} provine din urmatoarele tari {tari}')


# str(round(i['probability']*100, 5)) 
tari = [ i['country_id']  + ' cu probabilitatea ' +  "{:.3f}".format(i['probability']*100) + '%'  for i in probabilitati['country']]
tari = ", ".join(tari)
print(tari)

print(f'Numele {nume} provine din urmatoarele tari {tari}')