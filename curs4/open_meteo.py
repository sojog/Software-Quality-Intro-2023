import requests
import json
from pprint import pprint

formatted_url = 'https://api.open-meteo.com/v1/forecast?forecast_days=1&longitude=26.10&latitude=44.43&current_weather=true'

url = 'https://api.open-meteo.com/v1/forecast'
parameters = {
    'forecast_days':1,
    'longitude':26.10,
    'latitude':44.43,
    'current_weather':True
}

response = requests.get(url, parameters)

print(response.request.url)

print(response)
print(response.status_code)
print(response.content)



print(type(response.content))
response_dict =  json.loads(response.content)
pprint(response_dict)
print(type(response_dict))

print(response_dict['current_weather']['temperature'])