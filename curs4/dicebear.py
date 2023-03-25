import requests

url = 'https://api.dicebear.com/5.x/avataaars/svg'

response = requests.get(url)
print(response.content)



# deschid fisierul pentru scriere binara  w -> write + b -> binary
with open('avatar.svg', "wb") as f:
    f.write(response.content)


# deschid fisierul pentru scriere w -> write
with open('avatar2.svg', "w") as f:
    # binary -> str
    string = response.content.decode("utf-8")
    f.write(string)
