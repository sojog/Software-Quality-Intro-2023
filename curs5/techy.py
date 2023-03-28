""" HTTP request to generate cool tech-savvy sounding phrases easilyget 
"""
import requests

raspuns = requests.get("https://techy-api.vercel.app/api/text")
print(raspuns.content)

# a - append
# w - write
# r - read
# b - binary
# ab - deschidem un nou fisier pentru a face append + scriere in binar
with open('zicale.txt', 'ab') as file_handler:
    file_handler.write(raspuns.content)
    file_handler.write(b'\n')


