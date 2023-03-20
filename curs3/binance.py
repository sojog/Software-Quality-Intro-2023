import requests
import json

base_url = 'https://api1.binance.com'
'https://api2.binance.com'
'https://api3.binance.com'
'https://api4.binance.com'


path = '/api/v3/avgPrice?symbol=ETHBTC'
response = requests.get(base_url + path)
print(response.status_code)
print(response.content)
print(type(response.content))
r = json.loads(response.content)
print(r)
print(type(r))

print(r['price'])