import requests

url = 'https://api.dicebear.com/5.x/bottts/svg'

response = requests.get(url)
print(response.content)


# f = open('buna_dimineata.svg', "w")
# f.write("SALUT!!!")
# f.close()

with open('buna_dimineata.svg', "wb") as f:
    f.write(response.content)


