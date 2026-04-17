import requests
import json
url = 'https://api.chucknorris.io/jokes/random'
response = requests.get(url).json()
joke = response["value"]
print(joke)