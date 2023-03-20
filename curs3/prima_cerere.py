import requests




response = requests.get("https://www.link-academy.com/")
print(response)
print(response.status_code)
print(response.content)

