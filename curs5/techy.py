import requests

raspuns = requests.get("https://techy-api.vercel.app/api/text")
print(raspuns.content)

# a - append
# w - write
# r - read
# b - binary
with open('zicale.txt', 'ab') as file_handler:
    file_handler.write(raspuns.content)
    file_handler.write(b'\n')


